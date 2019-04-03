<?php
header('Content-Type: application/json; charset=utf-8');

$id = $_GET["id"];

echo json_encode(
	array(
		"id" => $id,
	)
);
?>