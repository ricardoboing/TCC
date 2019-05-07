<?php
include "../../class/ClienteServer.php";
include "../../util/util.php";

// Dados gerais
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
$pacote = "a";
$pacote .= ($domingo == "1"  || $domingo == 1)?  "1" : "0";
$pacote .= ($segunda == "1"  || $segunda == 1)?  "1" : "0";
$pacote .= ($terca == "1"    || $terca == 1)?    "1" : "0";
$pacote .= ($quarta == "1"   || $quarta == 1)?   "1" : "0";
$pacote .= ($quinta == "1"   || $quinta == 1)?   "1" : "0";
$pacote .= ($sexta == "1"    || $sexta == 1)?    "1" : "0";
$pacote .= ($sabado == "1"   || $sabado == 1)?   "1" : "0";

if ($somTocar == "1" || $somTocar == 1) {
	$pacote .= "1";

	$pacote .= formatar_digitos($somVolume, 3, 0);
	$pacote .= formatar_digitos($somTempo, 2, 0);
} else {
	$pacote .= "0";
}

$pacote .= formatar_digitos($horario, 4, 0);
$pacote .= formatar_digitos(strlen($nome), 2, 0);
$pacote .= substr($nome, 0, 100);

$clienteServer = new ClienteServer();

if ($clienteServer->criarConexao() == 0) {
	// FALHOU
	echo json_encode(false);
	return;
}
if ($clienteServer->conectar() == 0) {
	// FALHOU
	echo json_encode(false);
	return;
}
if ($clienteServer->enviar($pacote) == 0) {
	// FALHOU
	echo json_encode(false);
	return;
}

$respostaDoServidor = $clienteServer->ler(1);
$clienteServer->desconectar();

if ($respostaDoServidor != "1") {
	// FALHOU
	echo json_encode(false);
	return;
}

echo json_encode(true);

?>