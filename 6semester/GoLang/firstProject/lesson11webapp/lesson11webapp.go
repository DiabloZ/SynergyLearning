package lesson11webapp

import (
	"database/sql"
	_ "github.com/mattn/go-sqlite3"
	"html/template"
	"log"
	"net/http"
)

type Users struct {
	login    string
	password string
}

var users = map[int][]Users{}

func Main() {
	go createDB()
	fillUsersFromDB()
	mux := http.NewServeMux()
	mux.HandleFunc("/", index)
	mux.HandleFunc("/home", home)
	mux.HandleFunc("/login", login)
	mux.HandleFunc("/register", register)
	mux.HandleFunc("/create_card", createCard)
	err := http.ListenAndServe(":8080", mux)
	log.Fatal(err)
}

func fillUsersFromDB() {
	users[0] = append(users[0], Users{login: "admin", password: "admin"})
	// Подключение к базе данных
	db, err := sql.Open("sqlite3", "./test.db")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// Запрос на получение всех пользователей
	rows, err := db.Query("SELECT id, username, password FROM user")
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	for rows.Next() {
		var id int
		var username, password string
		if err := rows.Scan(&id, &username, &password); err != nil {
			log.Fatal(err)
		}
		users[id] = append(users[id], Users{login: username, password: password})
	}
	if err := rows.Err(); err != nil {
		log.Fatal(err)
	}
}

func createCard(writer http.ResponseWriter, request *http.Request) {
	ts, err := template.ParseFiles("./templates/create_card.html")
	if err != nil {
		http.Error(writer, err.Error(), http.StatusInternalServerError)
		log.Println(err.Error(), http.StatusInternalServerError)
		return
	}
	err = ts.Execute(writer, nil)
	if err != nil {
		http.Error(writer, err.Error(), http.StatusInternalServerError)
		log.Println(err.Error(), http.StatusInternalServerError)
		return
	}
}

func createDB() {
	// Подключение к базе данных
	db, err := sql.Open("sqlite3", "./test.db")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// Создание таблицы
	sqlStmt := `
	CREATE TABLE IF NOT EXISTS user (id INTEGER NOT NULL PRIMARY KEY, username TEXT, password TEXT);
	DELETE FROM user;
	`
	_, err = db.Exec(sqlStmt)
	if err != nil {
		log.Fatalf("%q: %s\n", err, sqlStmt)
	}
}

func register(writer http.ResponseWriter, request *http.Request) {
	ts, err := template.ParseFiles("./templates/register.html")
	if err != nil {
		http.Error(writer, err.Error(), http.StatusInternalServerError)
		log.Println(err.Error(), http.StatusInternalServerError)
		return
	}
	err = ts.Execute(writer, nil)
	if err != nil {
		http.Error(writer, err.Error(), http.StatusInternalServerError)
		log.Println(err.Error(), http.StatusInternalServerError)
		return
	}
	username := request.FormValue("username")
	password := request.FormValue("password")
	log.Println("Username:", username, "Password:", password)

	http.Redirect(writer, request, "/", http.StatusSeeOther)
}

func login(writer http.ResponseWriter, request *http.Request) {
	ts, err := template.ParseFiles("./templates/login.html")
	if err != nil {
		http.Error(writer, err.Error(), http.StatusInternalServerError)
		log.Println(err.Error(), http.StatusInternalServerError)
		return
	}

	if request.Method != http.MethodPost {
		err := ts.Execute(writer, nil)
		if err != nil {
			http.Error(writer, err.Error(), http.StatusInternalServerError)
			log.Println(err.Error(), http.StatusInternalServerError)
			return
		}
	}

	username := request.FormValue("username")
	password := request.FormValue("password")
	if username == "" || password == "" {
		return
	}
	isUserFound := false
	for i := range users {
		if users[i][0].login == username && users[i][0].password == password {
			log.Println("User found:", users[i][0].login)
			isUserFound = true
			break
		}
	}

	log.Println("Username:", username, "Password:", password)

	if isUserFound {
		http.Redirect(writer, request, "/home", http.StatusSeeOther)
		return
	} else {
		http.Error(writer, "Invalid username or password", http.StatusUnauthorized)
		log.Println("Invalid username or password")
		return
	}
}

func index(writer http.ResponseWriter, request *http.Request) {
	if request.URL.Path != "/" {
		http.NotFound(writer, request)
		log.Println("Not Found", request.URL.Path)
		return
	}

	ts, err := template.ParseFiles("./templates/index.html")
	if err != nil {
		http.Error(writer, err.Error(), http.StatusInternalServerError)
		log.Println(err.Error(), http.StatusInternalServerError)
		return
	}
	err = ts.Execute(writer, nil)
	if err != nil {
		http.Error(writer, err.Error(), http.StatusInternalServerError)
		log.Println(err.Error(), http.StatusInternalServerError)
		return
	}
}

func home(writer http.ResponseWriter, request *http.Request) {
	ts, err := template.ParseFiles("./templates/home.html")
	if err != nil {
		http.Error(writer, err.Error(), http.StatusInternalServerError)
		log.Println(err.Error(), http.StatusInternalServerError)
		return
	}
	err = ts.Execute(writer, nil)
	if err != nil {
		http.Error(writer, err.Error(), http.StatusInternalServerError)
		log.Println(err.Error(), http.StatusInternalServerError)
		return
	}

}
