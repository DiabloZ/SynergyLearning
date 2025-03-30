package lesson8_udp_server

import (
	"fmt"
	"net"
)

func startServer() {
	udp, err := net.ResolveUDPAddr("udp", ":8001")
	if err != nil {
		fmt.Print("Error: ", err)
	}
	conn, err := net.ListenUDP("udp", udp)
	if err != nil {
		fmt.Print("Error: ", err)
		return
	}

	for {
		var buf [1024]byte
		_, addr, err := conn.ReadFromUDP(buf[0:])
		if err != nil {
			fmt.Print("Error: ", err)
			return
		}
		fmt.Printf("server - Message: %s from %s\n", string(buf[0:]), addr)
		conn.WriteToUDP([]byte("Message received!!!\n"), addr)
	}
}
