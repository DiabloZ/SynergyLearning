package lesson5

import (
	"fmt"
	"time"
)

func Main() {
	student := Student2{name: "test", age: 12345}
	println(student.name, student.age)
	student.Greet()

	dog := Animal{species: "DOG", weight: 35.5}
	dog.Info()

	customer := Customer{
		name: "Some",
		address: Address{
			street:  "Lenina",
			city:    "Moscow",
			zipcode: "123-456",
		},
		phone: "+7123456789"}

	fmt.Println(customer)

	user := User{
		ID:        123,
		Name:      "SomeName",
		Email:     "1@2.com",
		Password:  "SomePass",
		CreatedAt: time.Now(),
	}

	user.Info()
	var test = new(Dogazavr)
	test.bread = ""
	test.name = ""
	dogozavr := Dogazavr{
		Animalz: Animalz{name: "zavr"},
		bread:   "Hleb",
	}
	dogozavr.Speak()

	dogorface := DogLikeConsumerOfInterface{
		name: "someName",
	}

	dogorface.Speak()
	var dogoFace AnimalLikeInterface = &dogorface
	dogoFace.Speak()

	var animals []AnimalReturnedString
	animals = append(animals, &DogWithAnimalString{notInterestingField: "123"})
	animals = append(animals, &CatWithAnimalString{someDifferentField: "321"})
	for _, animals := range animals {
		fmt.Println(animals.Speak())
	}
}

type Student2 struct {
	name string
	age  int
}

func (s *Student2) Greet() {
	println("hi, i am ", s.name, ". i have old ", s.age, ".")
}

type Printable interface {
	Print()
}

type Animal struct {
	species string
	weight  float32
}

func (a *Animal) Info() {
	fmt.Printf("Вид животного: %s, вес животного: %.2f kg\n", a.species, a.weight)
}

type Address struct {
	street  string
	city    string
	zipcode string
}

type Customer struct {
	name    string
	address Address
	phone   string
}

type User struct {
	ID        int
	Name      string
	Email     string
	Password  string
	CreatedAt time.Time
}

func (u *User) Info() {
	fmt.Print(
		"ID: ", u.ID, "\n",
		"Name: ", u.Name, "\n",
		"Email: ", u.Email, "\n",
		"Password: ", u.Password, "\n",
		"CreatedAt: ", u.CreatedAt, "\n",
	)
}

type Animalz struct {
	name string
}

func (a *Animalz) Speak() {
	fmt.Println("I am an animal")
}

type Dogazavr struct {
	Animalz
	bread string
}

type AnimalLikeInterface interface {
	Speak()
}

type DogLikeConsumerOfInterface struct {
	name string
}

func (receiver DogLikeConsumerOfInterface) Speak() {
	fmt.Println("GO GO GO")
}

type AnimalReturnedString interface {
	Speak() string
}

type DogWithAnimalString struct {
	notInterestingField string
}

func (d *DogWithAnimalString) Speak() string {
	return "GO GO GOZ"
}

type CatWithAnimalString struct {
	someDifferentField string
}

func (c *CatWithAnimalString) Speak() string {
	return "mao mao"
}
