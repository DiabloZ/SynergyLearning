package main

import (
	"fmt"
	"runtime"
	"time"
)
import _ "runtime"

func main() {
	var x int = 5
	fmt.Println(x)
	runtime.GOMAXPROCS(4)
	for i := 1; i <= 4; i++ {
		go worker(i)
	}
	time.Sleep(time.Second)
}

func worker(id int) {
	for i := 1; i <= 10; i++ {
		fmt.Printf("Поток %d: %d\n", id, i)
	}
}
