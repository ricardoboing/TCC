<?php
include "../../class/ClienteServer.php";
include "../../class/Pacote.php";

// Dados gerais
$id = explode(",", $_GET["id"]);

$pacote = "";
for ($c = 0; $c < count($id); $c++) {
	$pacote .= $id[$c];
}


echo $pacote;

$clienteServer = new ClienteServer();
$clienteServer->criarConexao();
$clienteServer->conectar();
$clienteServer->enviar($pacote);
$clienteServer->desconectar();
?>