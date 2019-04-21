<?php
// Dados gerais
$id = $_GET["id"];
$nome = $_GET["nome"];
$horario = $_GET["horario"];

// Dados sobre dias de acontecimento do evento
$segunda = $_GET["segunda"];
$terca = $_GET["terca"];
$quarta = $_GET["quarta"];
$quinta = $_GET["quinta"];
$sexta = $_GET["sexta"];
$sabado = $_GET["sabado"];
$domingo = $_GET["domingo"];

// Dados do som
$somTocar = $_GET["somTocar"];
$somVolume = $_GET["somVolume"];
$somTempo = $_GET["somTempo"];

// Formacao do pacote a ser enviado (de acordo com o protocolo definido)
$pacote = "c";

$clienteServer = new ClienteServer();
$clienteServer->criarConexao();
$clienteServer->conectar();
$clienteServer->enviar($pacote);
$clienteServer->desconectar();


?>