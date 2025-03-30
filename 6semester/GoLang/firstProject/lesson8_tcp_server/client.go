package lesson8_tcp_server

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"time"
)

func startClient() {
	cn, _ := net.Dial("tcp", "localhost:8000")
	for {
		rd := bufio.NewReader(os.Stdin)
		fmt.Printf("client - Enter text at %s: ", time.Now().Format(time.RFC3339))
		txt, _ := rd.ReadString('\n')
		fmt.Fprintf(cn, txt)
		msg, _ := bufio.NewReader(cn).ReadString('\n')
		fmt.Printf("client - Response from server at %s: %s", time.Now().Format(time.RFC3339), msg)
		fmt.Println("||||||||||||||||||||||||")
	}
}
