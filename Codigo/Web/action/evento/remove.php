<?php
include "../../class/ClienteServer.php";

// Dados gerais
$id = explode(",", $_GET["id"]);

$pacote = "remove event test";
for ($c = 0; $c < count($id); $c++) {
	$pacote .= $id[$c];
}

$clienteServer = new ClienteServer();
$clienteServer->criarConexao();
$clienteServer->conectar();
$clienteServer->enviar($pacote);
$clienteServer->desconectar();

$respostaDoServidor = true;

echo json_encode($respostaDoServidor);
?>