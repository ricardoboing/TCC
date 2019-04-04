<?php
include "class/ClienteServer.php";

$clienteServer = new ClienteServer();
echo $clienteServer->criarConexao();
echo $clienteServer->conectar();
echo $clienteServer->enviar("deu boa");
echo $clienteServer->desconectar();

?>