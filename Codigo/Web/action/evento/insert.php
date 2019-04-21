<?php
include "../../class/ClienteServer.php";

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
$pacote .= ($domingo == "1"  || $domingo == 1)? "1" : "0";
$pacote .= ($segunda == "1"  || $segunda == 1)?  "1" : "0";
$pacote .= ($terca == "1"    || $terca == 1)?    "1" : "0";
$pacote .= ($quarta == "1"   || $quarta == 1)?   "1" : "0";
$pacote .= ($quinta == "1"   || $quinta == 1)?   "1" : "0";
$pacote .= ($sexta == "1"    || $sexta == 1)?    "1" : "0";
$pacote .= ($sabado == "1"   || $sabado == 1)?   "1" : "0";

if ($somTocar == "1"  || $somTocar == 1) {
	$pacote .= "1";

	switch (strlen($somVolume)) {
		case 0:
			$pacote .= "000";
			break;
		case 1:
			$pacote .= "00".$somVolume;
			break;
		case 2:
			$pacote .= "0".$somVolume;
			break;
		case 3:
			$pacote .= $somVolume;
			break;
		default:
			$pacote .= substr($somVolume, 0, 2);
			break;
	}
	switch (strlen($somTempo)) {
		case 0:
			$pacote .= "00";
			break;
		case 1:
			$pacote .= "0".$somTempo;
			break;
		case 2:
			$pacote .= $somTempo;
			break;
		default:
			$pacote .= substr($somTempo, 0, 2);
			break;
	}
} else {
	$pacote .= "0";
}

switch (strlen($horario)) {
	case 4:
		$pacote .= $horario;
		break;
	case 3:
		$pacote .= "0".$horario;
		break;
	case 2:
		$pacote .= "00".$horario;
		break;
	case 1:
		$pacote .= "000".$horario;
		break;
	case 0:
		$pacote .= "0000";
		break;
	default:
		$pacote .= substr($horario, 0, 4);
		break;
}

if (strlen($nome) < 10) {
	$pacote .= "0";
}
$pacote .= strlen($nome);
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
if ($clienteServer->ler(1) != "1") {
	// FALHOU
	echo json_encode(false);
	return;
}

$clienteServer->desconectar();

echo json_encode(true);
?>