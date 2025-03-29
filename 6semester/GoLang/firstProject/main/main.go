package main

import (
	"firstProject/lesson2"
	"firstProject/lesson3"
	"firstProject/lesson4"
	"fmt"
	"runtime"
	"time"
)
import _ "runtime"

func main() {
	part1()

	lesson2.Main()
	lesson3.Main()
	lesson4.Main()
	lesson4.Main()

}

func part1() {
	var x int = 5
	fmt.Println(x)
	runtime.GOMAXPROCS(4)
	for i := 1; i <= 4; i++ {
		go worker(i)
	}
	time.Sleep(time.Second)
}

func worker(id int) int {
	for i := 1; i <= 10; i++ {
		fmt.Printf("Поток %d: %d\n", id, i)
	}
	return 0
}
