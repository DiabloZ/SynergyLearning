package main

import (
	"firstProject/lesson11webapp"
	"fmt"
	"runtime"
	"time"
)
import _ "runtime"

func main() {
	///part1()
	///lesson2.Main()
	///lesson3.Main()
	///lesson4.Main()
	///lesson4.Main()
	//lesson7.Main()

	//lesson8_tcp_server.Main()
	//lesson8_udp_server.Main()
	//lesson8http.Main()
	//lesson8validator.Main()
	//lesson9web.Main()
	//lesson10gorutines.Main()
	lesson11webapp.Main()
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
