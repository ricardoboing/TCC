<?php
include "../../class/ClienteServer.php";

// Dados gerais
$id = $_GET["id"];

$pacote = "b".$id;

$clienteServer = new ClienteServer();
$clienteServer->criarConexao();
$clienteServer->conectar();
$clienteServer->enviar($pacote);
$clienteServer->desconectar();

$respostaDoServidor = true;

echo json_encode($respostaDoServidor);
?>