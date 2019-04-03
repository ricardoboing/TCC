<?php
header('Content-Type: application/json; charset=utf-8');

$valor = $_GET["valor"];
$consumo = $_GET["consumo"];
$id = null; // Obter do BD apos o insert

echo json_encode(
	array(
		"id" => $id,
		"consumo" => $consumo,
		"valor" => $valor
	)
);
?>