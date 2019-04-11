<?php
header('Content-Type: application/json; charset=utf-8');

$valor = $_GET["valor"];

// Salva no servidor...
// Recebe resposta do servidor...
$respostaDoServidor = true;

echo json_encode($respostaDoServidor);
?>