package lesson8_tcp_server

import (
	"bufio"
	"fmt"
	"net"
	"strings"
	"time"
)

func startServer() {
	fmt.Println("StartServer")
	ln, _ := net.Listen("tcp", ":8000")
	cn, _ := ln.Accept()
	for {
		msg, _ := bufio.NewReader(cn).ReadString('\n')
		fmt.Printf("server - Message: %s at %s", time.Now().Format(time.RFC3339), string(msg))
		nmsg := strings.ToUpper(string(msg))
		cn.Write([]byte(nmsg + "\n"))
	}
}
