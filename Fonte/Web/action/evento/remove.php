<?php
include "../../class/ClienteServer.php";
include "../../util/util.php";

// Dados gerais
$id = explode(",", $_GET["id"]);
$numeroDeIds = count($id);

$pacote = "b";
$pacote .= codificar_inteiro($numeroDeIds);

for ($c = 0; $c < $numeroDeIds; $c++) {
	$pacote .= codificar_id($id[$c]);
}

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