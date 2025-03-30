package lesson8_tcp_server

func Main() {
	go startServer()
	startClient()
}
