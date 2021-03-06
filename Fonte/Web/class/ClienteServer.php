<?php
header("Content-type: text/html;charset=utf-8");

class ClienteServer {
	private $host, $port;
	private $socket;

	function ClienteServer() {
		$this->host = "192.168.50.179";//"192.168.25.16";//"192.168.50.179";
		$this->port = 8086;
	}
	
	function criarConexao() {
		$this->socket = socket_create(AF_INET, SOCK_STREAM, 0);
		return $this->socket? 1 : 0;
	}
	function conectar() {
		return socket_connect($this->socket, $this->host, $this->port)? 1 : 0;
	}
	function desconectar() {
		return socket_close($this->socket)? 1 : 0;
	}
	function enviar($dado) {
		return socket_write ($this->socket, $dado, strlen($dado))? 1 : 0;
	}
	function ler($bytes) {
		return socket_read ($this->socket, $bytes);
	}
};
?>