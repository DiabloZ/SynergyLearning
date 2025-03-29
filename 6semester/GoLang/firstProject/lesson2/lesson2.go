package lesson2

import (
	"container/list"
	"fmt"
)

func Main() {
	//part2()
	//part3()
	//part3switch()
	//part3for()
	//part3fori()
	//part3ForIBreak()
	//var answ4 = part4FunctionWithParameters(2, 2)
	//fmt.Println(answ4)
	//fmt.Println(part4FunctionWithParameters(10, 111))
	//var stdnt = Student{age: answ4, name: "someName"}
	//stdnt.Part5GreetAnExtensionFunction()
	//part5Arrays()
	//part5Arrays2()
	//part5Slices()
	//part5Matrix()
	//part5List()
	//part6Pointer()
	part6Pointer2()
}

func part6Pointer2() {
	a := 54
	var b *int = &a
	fmt.Println(a)
	fmt.Println(b)

}

func part6Pointer() {
	a := 0xFF
	b := 0x9D
	fmt.Println(a, b)
	fmt.Printf("%T\n", a)
	fmt.Printf("%T\n", b)
}

func part5List() {
	check := list.New()
	check.PushBack("some")
	check.PushBack(10)
	check.PushBack(false)

	fmt.Println(check)
	element1 := check.Front()
	element2 := check.Back()
	fmt.Println(element1)
	fmt.Println(element2)
	check.Remove(check.Back())
	fmt.Println(check.Back())
}

func part5Matrix() {
	matrix := [][]int{{100, 112}, {234, 6551}}
	fmt.Println(matrix)
}

func part5Slices() {
	mySlice := []int{123, 321, 1, 2, 3}
	fmt.Println(mySlice)
	mySlice = append(mySlice, 1000)
	fmt.Println(mySlice)

	slice := mySlice[1:3]
	fmt.Println(slice)
}

func part5Arrays2() {
	var digits = [5]int{12, 23, 42, 12, 2}
	fmt.Println(digits)
}

func part5Arrays() {
	var numbers [5]int
	for i := 0; i < 5; i++ {
		numbers[i] = i
		fmt.Println(numbers)
	}
}

func (s *Student) Part5GreetAnExtensionFunction() {
	fmt.Printf("!!! name:%s, age:%d", s.name, s.age)
}

type Student struct {
	name string
	age  int
}

func part4FunctionWithParameters(i int, i2 int) int {
	return i + i2
}

func part3ForIBreak() {
	i := 10
	for {
		if i <= 5 {
			break
		}
		fmt.Println(i)
		i--
	}
}

func part3fori() {
	i := 1
	for i <= 5 {
		fmt.Println(i)
		i++
	}
}

func part3for() {
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}
}

func part3switch() {
	var day = "Friday"
	switch day {
	case "Monday":
		fmt.Println("День тяжелеый")
	case "Friday":
		fmt.Println("Пятница!")
	case day:
		fmt.Println("Other day")
	}
}

func part3() {
	var num = 10
	if num == 10 {
		fmt.Printf("num = 10")
	} else if num >= 5 {
		fmt.Printf("num > 5")
	} else {
		fmt.Printf("num < 5")
	}
}

func part2() {
	num := 10
	var num2 int = 10
	fmt.Println(num, num2)
	var (
		number int
		word   string
		eq     bool
	)
	fmt.Println(number, word, eq)
}
