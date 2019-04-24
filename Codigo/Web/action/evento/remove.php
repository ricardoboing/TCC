<?php
include "../../class/ClienteServer.php";

// Dados gerais
$id = explode(",", $_GET["id"]);
$pacote = "b";

for ($c = 0; $c < count($id); $c++) {
	switch (strlen($id[$c])) {
		case 3:
			$pacote .= "0";
			break;
		case 2:
			$pacote .= "00";
			break;
		case 1:
			$pacote .= "000";
			break;
		default:
			break;
	}

	$pacote .= $id[$c];
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