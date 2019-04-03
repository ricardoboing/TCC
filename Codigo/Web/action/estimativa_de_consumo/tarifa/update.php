<?php
header('Content-Type: application/json; charset=utf-8');

$id = $_GET["id"];
$valor = $_GET["valor"];
$consumo = $_GET["consumo"];

echo json_encode(
	array(
		"id" => $id,
		"consumo" => $consumo,
		"valor" => $valor
	)
);
?>