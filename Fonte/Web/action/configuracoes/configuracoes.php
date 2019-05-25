<?php
include "../../class/ClienteServer.php";
include "../../util/util.php";

$noIotVelocidade = $_GET["noIotVelocidade"];
$noIotTempoAtividade = $_GET["noIotTempoAtividade"];
$bateriaCapacidade = $_GET["bateriaCapacidade"];

$consumoAtivado = $_GET["consumoAtivado"];
$consumoDesativado = $_GET["consumoDesativado"];


$pacote = "k";
$pacote .= formatar_digitos($noIotVelocidade, 3, "0");
$pacote .= formatar_digitos($noIotTempoAtividade, 3, "0");
$pacote .= formatar_digitos($bateriaCapacidade, 4, "0");
$pacote .= formatar_digitos($consumoAtivado, 5, "0");
$pacote .= formatar_digitos($consumoDesativado, 5, "0");

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