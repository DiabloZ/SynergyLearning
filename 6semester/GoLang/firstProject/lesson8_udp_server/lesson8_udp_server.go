package lesson8_udp_server

func Main() {
	go startServer()
	startClient()
}
