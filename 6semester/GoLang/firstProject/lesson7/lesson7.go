package lesson7

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"sync"
)

func Main() {
	//fmt.Println(Sum(5, 10))
	//OpenFile()
	//BuggerPrintLn()
	DebugMultyTread()
}

var mu sync.Mutex
var wg sync.WaitGroup

func DebugMultyTread() {
	data := []int{1, 2, 3, 4, 5}
	for i := 0; i < len(data); i++ {
		wg.Add(1)
		go processData(data, i+1)
	}
	wg.Wait()
	fmt.Println("All goroutines are done")
}

func processData(data []int, id int) {
	for i := 1; i <= 10; i++ {
		mu.Lock()
		fmt.Printf("Поток %d: %d\n", id, i)
		mu.Unlock()
	}
	wg.Done()
}

func BuggerPrintLn() {
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	for i := 0; i < 9999999999; i++ {
		fmt.Fprintf(w, "%d\n", i)
	}
}

func OpenFile() {
	_, err := os.Stat("file.txt")
	if os.IsNotExist(err) {
		fmt.Print("File is not exist: ", err)
		return
	}
	file, err := os.Open("file.txt")
	if err != nil {
		println("Open file error")
		return
	}
	defer file.Close()
	buf := make([]byte, 1024)
	for {
		n, err := file.Read(buf)
		if err == io.EOF {
			return
		} else if err != nil {
			fmt.Println("Open filer error: ", err)
			return
		}
		fmt.Println(string(buf[:n]))
	}
}

func Sum(a, b int) int {
	return 0
}
