<?php
include "../../class/ClienteServer.php";
include "../../util/util.php";

$operacao = $_GET["operacao"];
$comando = "";

switch ($operacao) {
	case "parar":
		$comando = "a";
		break;
	case "tocar":
		$comando = "b";
		$comando .= formatar_digitos($_GET["valor"], 3, "0");
		break;
	case "alterar_volume":
		$comando = "c";
		$comando .= formatar_digitos($_GET["valor"], 3, "0");
		break;
	default:
		break;
}

$pacote = "g";
$pacote .= $comando;

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