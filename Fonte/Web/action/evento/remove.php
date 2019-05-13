<?php
include "../../class/ClienteServer.php";
include "../../util/util.php";

// Dados gerais
$id = explode(",", $_GET["id"]);
$pacote = "b";
$pacote .= formatar_digitos(count($id), 3, 0);

for ($c = 0; $c < count($id); $c++) {
	$pacote .= formatar_digitos($id[$c], 10, 0);
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