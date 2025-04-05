package lesson9web

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/gorilla/mux"
	"github.com/patrickmn/go-cache"
	"html/template"
	"net/http"
	"time"
)

func Main() {
	cacheOfLoad()
	//htmlMain()
	//startRestApiServer()
	//startWebServer()
}

func cacheOfLoad() {
	newCache := cache.New(5*time.Minute, 10*time.Minute)
	newCache.Set("key", "value", cache.DefaultExpiration)
	newCache.Set("anotherOne", 43, cache.NoExpiration)
	cache, found := newCache.Get("key")
	if found {
		fmt.Println(cache)
	}
}

func htmlMain() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", indexHandler)
	mux.HandleFunc("/second", secondIndex)
	http.ListenAndServe(":8080", mux)
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		http.NotFound(w, r)
		return
	}
	ts, _ := template.ParseFiles("./index.html")
	ts.Execute(w, nil)
}

func secondIndex(w http.ResponseWriter, r *http.Request) {
	ts, _ := template.ParseFiles("./second.html")
	ts.Execute(w, nil)
}

func startRestApiServer() {
	router := gin.Default()
	router.GET("/albums", getAlbums)
	router.GET("/albums/:id", getAlbumByID)
	router.POST("/albums", postAlbum)
	router.PUT("/albums/:id", updateAlbum)
	router.DELETE("/albums/:id", deleteAlbum)
	err := router.Run("localhost:8080")
	if err != nil {
		return
	}
}

func deleteAlbum(context *gin.Context) {
	id := context.Param("id")
	for i, a := range albums {
		if a.ID == id {
			albums = append(albums[:i], albums[i+1:]...)
			context.IndentedJSON(http.StatusOK, gin.H{"message": "album deleted"})
			return
		}
	}
	context.IndentedJSON(http.StatusNotFound, gin.H{"message": "album not found"})
}

func updateAlbum(context *gin.Context) {
	id := context.Param("id")
	var updatedAlbum Album
	if err := context.BindJSON(&updatedAlbum); err != nil {
		return
	}
	for i, a := range albums {
		if a.ID == id {
			albums[i] = updatedAlbum
			context.IndentedJSON(http.StatusOK, updatedAlbum)
			return
		}
	}
	context.IndentedJSON(http.StatusNotFound, gin.H{"message": "album not found"})
}

func postAlbum(context *gin.Context) {
	var newAlbum Album
	if err := context.BindJSON(&newAlbum); err != nil {
		return
	}
	albums = append(albums, newAlbum)
	context.IndentedJSON(http.StatusCreated, newAlbum)
}

func getAlbumByID(context *gin.Context) {
	id := context.Param("id")
	for _, a := range albums {
		if a.ID == id {
			context.IndentedJSON(http.StatusOK, a)
			return
		}
	}
	context.IndentedJSON(http.StatusNotFound, gin.H{"message": "album not found"})
}

func getAlbums(context *gin.Context) {
	context.IndentedJSON(http.StatusOK, albums)
}

type Album struct {
	ID     string  `json:"id"`
	Title  string  `json:"title"`
	Artist string  `json:"artist"`
	Price  float64 `json:"price"`
}

var albums = []Album{
	{ID: "1", Title: "Album 1", Artist: "Artist 1", Price: 10.0},
	{ID: "2", Title: "Album 2", Artist: "Artist 2", Price: 20.0},
	{ID: "3", Title: "Album 3", Artist: "Artist 3", Price: 30.0},
	{ID: "4", Title: "Album 4", Artist: "Artist 4", Price: 40.0},
	{ID: "5", Title: "Album 5", Artist: "Artist 5", Price: 50.0},
}

func startWebServer() {
	r := mux.NewRouter()
	r.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello World!!!"))
	})
	http.ListenAndServe(":8080", r)
}
