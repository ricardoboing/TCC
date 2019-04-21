<?php
include "../../../class/ClienteServer.php";
header('Content-Type: application/json; charset=utf-8');

$valor = $_GET["valor"];

$pacote = "d";
if (strlen($valor) > 9) {
	$pacote .= "9";
} else {
	$pacote .= strlen($valor);
}
$pacote .= substr($valor, 0, 9);

$clienteServer = new ClienteServer();
$clienteServer->criarConexao();
$clienteServer->conectar();
$clienteServer->enviar($pacote);
$clienteServer->desconectar();

// Recebe resposta do servidor...
$respostaDoServidor = true;

echo json_encode($respostaDoServidor);
?>