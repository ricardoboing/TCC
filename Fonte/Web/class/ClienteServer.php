<?php
class ClienteServer {
	private $host, $port;
	private $socket;

	function ClienteServer() {
		$this->host = "192.168.50.179";//"192.168.25.6";//;
		$this->port = 8082;
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
		$lengthDado = strlen($dado);
		$dado = $lengthDado.$dado;

		if ($lengthDado < 10) {
			$dado = "0".$dado;
		}
		if ($lengthDado < 100) {
			$dado = "0".$dado;
		}

		return socket_write ($this->socket, $dado, strlen($dado))? 1 : 0;
	}
	function ler($bytes) {
		return socket_read ($this->socket, $bytes);
	}
};
?>