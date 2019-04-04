<?php
class ClienteServer {
	private $host, $port;
	private $socket;

	function ClienteServer() {
		$this->host = "yyy.yyy.yyy.yyy";
		$this->port = 8083;
	}
	
	function criarConexao() {
		$this->socket = socket_create(AF_INET, SOCK_STREAM, 0);
		return $this->socket ? 0 : 1;
	}
	function conectar() {
		return socket_connect($this->socket, $this->host, $this->port)? 0 : 1;
	}
	function desconectar() {
		return socket_close($this->socket)? 0 : 1;
	}
	function enviar($dado) {
		return socket_write($this->socket, $dado, strlen($dado))? 0 : 1;
	}
}
?>