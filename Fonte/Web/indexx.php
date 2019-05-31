<!DOCTYPE html>
<html>
<?php include_once "class/ClienteServer.php"; ?>
<?php include_once "include/head.php"; ?>
<?php
	$pacote = "h";
	$clienteServer = new ClienteServer();
	
	$sucesso = $clienteServer->criarConexao();
	
	if ($sucesso) {
		$sucesso = $clienteServer->conectar();
	}
	if ($sucesso) {
		$sucesso = $clienteServer->enviar($pacote);
	}
	if ($sucesso) {
		$diaHoraAtivado  = $clienteServer->ler(2);
		$diaHoraAtivado .= ":";
		$diaHoraAtivado .= $clienteServer->ler(2);
		
		$diaHoraDesativado  = $clienteServer->ler(2);
		$diaHoraDesativado .= ":";
		$diaHoraDesativado .= $clienteServer->ler(2);
		
		$diaConsumo  = $clienteServer->ler(2);
		$diaConsumo .= ".";
		$diaConsumo .= $clienteServer->ler(2);
		
		$mesHoraAtivado = $diaHoraAtivado*30;
		$mesHoraDesativado = $diaHoraDesativado*30;
		$mesConsumo = $diaConsumo*30;

		$duracaoCarregado  = $clienteServer->ler(2);
		$duracaoCarregado .= ".";
		$duracaoCarregado .= $clienteServer->ler(2);

		$duracaoConsumido  = $clienteServer->ler(2);
		$duracaoConsumido .= ".";
		$duracaoConsumido .= $clienteServer->ler(2);

		$duracaoRestante  = $clienteServer->ler(2);
		$duracaoRestante .= ".";
		$duracaoRestante .= $clienteServer->ler(2);
		
		$clienteServer->desconectar();
	} else {
		$mensagemErro = "FALHA/ERRO";

		$diaHoraAtivado = $mensagemErro;
		$diaHoraDesativado = $mensagemErro;
		$diaConsumo = $mensagemErro;

		$mesHoraAtivado = $mensagemErro;
		$mesHoraDesativado = $mensagemErro;
		$mesConsumo = $mensagemErro;
		
		$duracaoCarregado = $mensagemErro;
		$duracaoConsumido = $mensagemErro;
		$duracaoRestante  = $mensagemErro;
	}
?>
<body>
	<header>
		<span>CONSUMO ESTIMATIVO DA BATERIA</span>
	</header>
	<main class="estimativa_de_consumo">
		<section>
			<div class="titulo">
				<span>Consumo diário</span>
			</div>
			<table>
				<tr>
					<th>
						<span>HORAS (ATIVADO)</span>
					</th>
					<td>
						<span><?php echo $diaHoraAtivado; ?></span>
					</td>
				</tr>
				<tr>
					<th>
						<span>HORAS (DESATIVADO)</span>
					</th>
					<td>
						<span><?php echo $diaHoraDesativado; ?></span>
					</td>
				</tr>
				<tr>
					<th>
						<span>kWH</span>
					</th>
					<td>
						<span><?php echo $diaConsumo; ?></span>
					</td>
				</tr>
			</table>
		</section>
		<section>
			<div class="titulo">
				<span>Consumo mensal</span>
			</div>
			<table>
				<tr>
					<th>
						<span>HORAS (ATIVADO)</span>
					</th>
					<td>
						<span><?php echo $mesHoraAtivado; ?></span>
					</td>
				</tr>
				<tr>
					<th>
						<span>HORAS (DESATIVADO)</span>
					</th>
					<td>
						<span><?php echo $mesHoraDesativado; ?></span>
					</td>
				</tr>
				<tr>
					<th>
						<span>kWH</span>
					</th>
					<td>
						<span><?php echo $mesConsumo; ?></span>
					</td>
				</tr>
			</table>
		</section>
		<section>
			<div class="titulo">
				<span>Tempo de duração (em horas)</span>
			</div>
			<table>
				<tr>
					<th>
						<span>CARREGADO</span>
					</th>
					<td>
						<span><?php echo $duracaoCarregado; ?></span>
					</td>
				</tr>
				<tr>
					<th>
						<span>CONSUMIDO</span>
					</th>
					<td>
						<span><?php echo $duracaoConsumido; ?></span>
					</td>
				</tr>
				<tr>
					<th>
						<span>RESTANTES</span>
					</th>
					<td>
						<span><?php echo $duracaoRestante; ?></span>
					</td>
				</tr>
			</table>
			<button>REINICIAR</button>
		</section>
	</main>
	<footer>
		<ul>
			<li data-active="active">
				<a href="javascript: void(0);">INÍCIO</a>
			</li>
			<li>
				<a href="controle.php">CONTROLE</a>
			</li>
			<li>
				<a href="agenda.php">AGENDA</a>
			</li>
			<li>
				<a href="configuracoes.php?page=index">CONFIG.</a>
			</li>
		</ul>
	</footer>
</body>
<?php include_once "include/scripts.php"; ?>
</html>