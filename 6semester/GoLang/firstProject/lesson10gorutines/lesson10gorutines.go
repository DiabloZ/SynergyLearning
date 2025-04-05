package lesson10gorutines

import (
	"fmt"
	"sync"
	"time"
)

func Main() {
	//goRutinesSync()
	//channels()
	//parallels()
	syncParallels()
}

var mutex = sync.Mutex{}
var counter = 0

func syncParallels() {

	for i := 0; i < 10; i++ {
		go incrimentCounter()
	}
	time.Sleep(100 * time.Microsecond)
	fmt.Println(counter)
}

func incrimentCounter() {
	mutex.Lock()
	counter++
	mutex.Unlock()
}

func parallels() {
	go say("Hello")
	go say("World")
	go multiply(8)
	go multiply(12)
	go multiply(100)
	time.Sleep(100 * time.Millisecond)
}
func multiply(d int) {
	if d < 10 {
		fmt.Println(10 * d)
	} else {
		fmt.Println(100 * d)
	}
}

func say(s string) {
	for i := 0; i < 5; i++ {
		fmt.Println(s)
	}
}

func channels() {
	//buffered
	ch := make(chan int)
	ch <- 10
	go func() {
		ch <- 10
	}()
	x := <-ch
	fmt.Println(x)

	//not buffered
	//???
}

func goRutinesSync() {
	result := make(chan int)
	go sum(result)

	go sum(result)
	x, y := <-result, <-result
	fmt.Println(x + y)
}

func sum(c chan int) {
	total := 0
	for i := 0; i <= 100; i++ {
		total += i
	}
	c <- total
}
