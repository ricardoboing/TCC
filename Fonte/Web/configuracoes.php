<!DOCTYPE html>
<html>
<?php
include_once "class/ClienteServer.php";
include_once "include/head.php";
?>

<?php
	$pacote = "j";
	$clienteServer = new ClienteServer();
	$clienteServer->criarConexao();
	$clienteServer->conectar();
	$clienteServer->enviar($pacote);

	$velocidade = "\"".intval($clienteServer->ler(3))."\"";
	$tempoDeAtividade = "\"".intval($clienteServer->ler(3))."\"";
	$capacidadeDaBateria = "\"".intval($clienteServer->ler(4))."\"";
	$consumoAtivado = "\"".intval($clienteServer->ler(5))."\"";
	$consumoDesativado = "\"".intval($clienteServer->ler(5))."\"";

	$clienteServer->desconectar();
?>
<body>
	<header>
		<span>CONFIGURAÇÕES</span>
	</header>
	<main class="configuracoes">
		<form>
			<section class="evento">
				<div class="titulo">
					<span>Agendamento</span>
				</div>
				<div>
					<label for="no_iot_tempo_atividade">Tempo de ida + volta (ms):</label>
					<input type="text" class="number" id="no_iot_tempo_atividade" placeholder="0" value=<?php echo $tempoDeAtividade; ?>>
				</div>
				<div>
					<label for="no_iot_velocidade">Velocidade:</label>
					<input type="range" id="no_iot_velocidade" value=<?php echo $velocidade; ?>>
				</div>
			</section>
			<section class="evento">
				<div class="titulo">
					<span>Bateria</span>
				</div>
				<div>
					<label for="bateria_capacidade">Capacidade (mA):</label>
					<input type="text" class="number" id="bateria_capacidade" placeholder="0" value=<?php echo $capacidadeDaBateria; ?>>
				</div>
			</section>
			<section class="evento">
				<div class="titulo">
					<span>Consumo de energia</span>
				</div>
				<div>
					<label for="consumo_ativado">Consumo ativado (mA):</label>
					<input type="text" class="number" id="consumo_ativado" placeholder="0" value=<?php echo $consumoAtivado; ?>>
				</div>
				<div>
					<label for="consumo_desativado">Consumo desativado (mA):</label>
					<input type="text" class="number" id="consumo_desativado" placeholder="0" value=<?php echo $consumoDesativado; ?>>
				</div>
			</section>
		</form>
	</main>
	<footer>
		<ul>
			<li>
				<a href="javascript: void(0);" class="salvar" data-href="index.php" disabled>SALVAR</a>
			</li>
			<li>
				<a href="index.php" class="cancelar">CANCELAR</a>
			</li>
		</ul>
	</footer>
</body>
<?php include_once "include/scripts.php"; ?>
</html>