package lesson8_udp_server

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func startClient() {
	udp, err := net.ResolveUDPAddr("udp", "localhost:8001")
	if err != nil {
		fmt.Print("Error: ", err)
		return
	}
	conn, err := net.DialUDP("udp", nil, udp)
	if err != nil {
		fmt.Print("Error: ", err)
		return
	}
	for {
		reader := bufio.NewReader(os.Stdin)
		for {
			fmt.Print("client - Enter text: ")
			msg, _ := reader.ReadString('\n')
			conn.Write([]byte(msg))
			var buf [1024]byte
			_, _, err := conn.ReadFromUDP(buf[0:])
			if err != nil {
				fmt.Print("Error: ", err)
				return
			}
			fmt.Printf("client - Response from server: %s\n", string(buf[0:]))
			fmt.Println("||||||||||||||||||||||||")
		}
	}
}
