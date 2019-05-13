<?php
include "../../class/ClienteServer.php";
include "../../util/util.php";

// Dados gerais
$id = $_GET["id"];
$nome = $_GET["nome"];
$horario = $_GET["horario"];

$lengthNome = strlen($nome);

// Dados sobre dias de acontecimento do evento
$domingo = ($_GET["domingo"] == "1")? "1" : "0";
$segunda = ($_GET["segunda"] == "1")? "1" : "0";
$terca   = ($_GET["terca"]   == "1")? "1" : "0";
$quarta  = ($_GET["quarta"]  == "1")? "1" : "0";
$quinta  = ($_GET["quinta"]  == "1")? "1" : "0";
$sexta   = ($_GET["sexta"]   == "1")? "1" : "0";
$sabado  = ($_GET["sabado"]  == "1")? "1" : "0";

// Dados do som
$somHabilitado = $_GET["somTocar"];
$somVolume = $_GET["somVolume"];
$somTempo = $_GET["somTempo"];

// Formacao do pacote a ser enviado (de acordo com o protocolo definido)
if ($somHabilitado == "1") {
	$pacote = "C";
} else {
	$pacote = "c";
}
$pacote .= codificar_id($id);
$pacote .= codificar_dias_da_semana(
	$domingo,
	$segunda,
	$terca,
	$quarta,
	$quinta,
	$sexta,
	$sabado
);

if ($somHabilitado) {
	$pacote .= codificar_som($somVolume,$somTempo);
}
$pacote .= codificar_horario(
	substr($horario,0,2),
	substr($horario,2,4)
);

$pacote .= codificar_length_nome($lengthNome);
$pacote .= substr($nome, 0, 30);

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