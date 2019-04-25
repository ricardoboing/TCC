<!DOCTYPE html>
<html>
<?php include "class/ClienteServer.php"; ?>
<?php include_once "include/head.php"; ?>
<?php
	$pacote = "e";
	$clienteServer = new ClienteServer();
	$clienteServer->criarConexao();
	$clienteServer->conectar();
	$clienteServer->enviar($pacote);

	$pacote = $clienteServer->ler(19);

	$clienteServer->desconectar();

	//00001111 00001111 000

	// CARRINHO
	$carrinhoDiaHora = substr($pacote, 0, 2).":".substr($pacote, 2, 2);
	$carrinhoMesHora = $carrinhoDiaHora*30;
	$carrinhoAnoHora = $carrinhoMesHora*12;

	$carrinhoDiaConsumo = substr($pacote, 4, 2).".".substr($pacote, 6, 2);
	$carrinhoMesConsumo = $carrinhoDiaConsumo*30;
	$carrinhoAnoConsumo = $carrinhoMesConsumo*12;

	$carrinhoDiaValorFinanceiro = 0;
	$carrinhoMesValorFinanceiro = 0;
	$carrinhoAnoValorFinanceiro = 0;

	// FOG
	$fogDiaHora = substr($pacote, 8, 2).":".substr($pacote, 10, 2);
	$fogMesHora = $fogDiaHora*30;
	$fogAnoHora = $fogMesHora*12;

	$fogDiaConsumo = substr($pacote, 12, 2).".".substr($pacote, 14, 2);
	$fogMesConsumo = $fogDiaConsumo*30;
	$fogAnoConsumo = $fogMesConsumo*12;

	$fogDiaValorFinanceiro = 0;
	$fogMesValorFinanceiro = 0;
	$fogAnoValorFinanceiro = 0;

	// TOTAL
	$totalDiaHora = "-";
	$totalMesHora = "-";
	$totalAnoHora = "-";

	$totalDiaConsumo = $carrinhoDiaConsumo + $fogDiaConsumo;
	$totalMesConsumo = $carrinhoMesConsumo + $fogMesConsumo;
	$totalAnoConsumo = $carrinhoAnoConsumo + $fogAnoConsumo;

	$totalDiaValorFinanceiro = 0;
	$totalMesValorFinanceiro = 0;
	$totalAnoValorFinanceiro = 0;

	$valorTarifa = substr($pacote, 16, 3);
	$valorTarifa = intval($valorTarifa);
?>
<body>
	<header>
		<span>ESTIMATIVA DE CONSUMO</span>
	</header>
	<main class="estimativa_de_consumo">
		<section>
			<div class="titulo">
				<span>Carrinho</span>
			</div>
			<table id="table_consumo_carrinho">
				<tr class="head">
					<th>
						<span></span>
					</th>
					<th>
						<span>DIA</span>
					</th>
					<th>
						<span>MÊS</span>
					</th>
					<th>
						<span>ANO</span>
					</th>
				</tr>
				<tr class="tempo">
					<th>
						<span>HORAS</span>
					</th>
					<td class="dia">
						<span><?php echo $carrinhoDiaHora; ?></span>
					</td>
					<td class="mes">
						<span><?php echo $carrinhoMesHora; ?></span>
					</td>
					<td class="ano">
						<span><?php echo $carrinhoAnoHora; ?></span>
					</td>
				</tr>
				<tr class="consumo">
					<th>
						<span>kWH</span>
					</th>
					<td class="dia">
						<span><?php echo $carrinhoDiaConsumo; ?></span>
					</td>
					<td class="mes">
						<span><?php echo $carrinhoMesConsumo; ?></span>
					</td>
					<td class="ano">
						<span><?php echo $carrinhoAnoConsumo; ?></span>
					</td>
				</tr>
				<tr class="valor_financeiro">
					<th>
						<span>R$</span>
					</th>
					<td class="dia">
						<span><?php echo $carrinhoDiaValorFinanceiro; ?></span>
					</td>
					<td class="mes">
						<span><?php echo $carrinhoMesValorFinanceiro; ?></span>
					</td>
					<td class="ano">
						<span><?php echo $carrinhoAnoValorFinanceiro; ?></span>
					</td>
				</tr>
			</table>
			<div class="titulo">
				<span>Fog</span>
			</div>
			<table id="table_consumo_fog">
				<tr class="head">
					<th>
						<span></span>
					</th>
					<th>
						<span>DIA</span>
					</th>
					<th>
						<span>MÊS</span>
					</th>
					<th>
						<span>ANO</span>
					</th>
				</tr>
				<tr class="tempo">
					<th>
						<span>HORAS</span>
					</th>
					<td class="dia">
						<span><?php echo $fogDiaHora; ?></span>
					</td>
					<td class="mes">
						<span><?php echo $fogMesHora; ?></span>
					</td>
					<td class="ano">
						<span><?php echo $fogAnoHora; ?></span>
					</td>
				</tr>
				<tr class="consumo">
					<th>
						<span>kWH</span>
					</th>
					<td class="dia">
						<span><?php echo $fogDiaConsumo; ?></span>
					</td>
					<td class="mes">
						<span><?php echo $fogMesConsumo; ?></span>
					</td>
					<td class="ano">
						<span><?php echo $fogAnoConsumo; ?></span>
					</td>
				</tr>
				<tr class="valor_financeiro">
					<th>
						<span>R$</span>
					</th>
					<td class="dia">
						<span><?php echo $fogDiaValorFinanceiro; ?></span>
					</td>
					<td class="mes">
						<span><?php echo $fogMesValorFinanceiro; ?></span>
					</td>
					<td class="ano">
						<span><?php echo $fogAnoValorFinanceiro; ?></span>
					</td>
				</tr>
			</table>
			<div class="titulo">
				<span>Total</span>
			</div>
			<table id="table_consumo_total">
				<tr class="head">
					<th>
						<span></span>
					</th>
					<th>
						<span>DIA</span>
					</th>
					<th>
						<span>MÊS</span>
					</th>
					<th>
						<span>ANO</span>
					</th>
				</tr>
				<!--
				<tr class="tempo">
					<th>
						<span>HORAS</span>
					</th>
					<td class="dia">
						<span><?php echo $totalDiaHora; ?></span>
					</td>
					<td class="mes">
						<span><?php echo $totalMesHora; ?></span>
					</td>
					<td class="ano">
						<span><?php echo $totalAnoHora; ?></span>
					</td>
				</tr>
				-->
				<tr class="consumo">
					<th>
						<span>kWH</span>
					</th>
					<td class="dia">
						<span><?php echo $totalDiaConsumo; ?></span>
					</td>
					<td class="mes">
						<span><?php echo $totalMesConsumo; ?></span>
					</td>
					<td class="ano">
						<span><?php echo $totalAnoConsumo; ?></span>
					</td>
				</tr>
				<tr class="valor_financeiro">
					<th>
						<span>R$</span>
					</th>
					<td class="dia">
						<span><?php echo $totalDiaValorFinanceiro; ?></span>
					</td>
					<td class="mes">
						<span><?php echo $totalMesValorFinanceiro; ?></span>
					</td>
					<td class="ano">
						<span><?php echo $totalAnoValorFinanceiro; ?></span>
					</td>
				</tr>
			</table>
			<div class="titulo">
				<span>Tarifa</span>
			</div>
			<table id="tarifa">
				<tr class="head">
					<th>
						<span>VALOR (R$)</span>
					</th>
					<th colspan="2">
						<span>CONSUMO (kWH)</span>
					</th>
				</tr>
				<tr>
					<td>
						<input type="number" name="" min="0" value=<?php echo "\"".$valorTarifa."\""; ?> >
					</td>
					<td>
						<input type="number" value="1" disabled="">
					</td>
					<td>
						<button class="green">OK</button>
					</td>
				</tr>
			</table>
		</section>
	</main>
	<footer>
		<ul>
			<li>
				<a href="javascript: void(0);">ESTIMATIVA DE CONSUMO</a>
			</li>
			<li>
				<a href="eventos.php">HORÁRIOS</a>
			</li>
		</ul>
	</footer>
</body>
<?php include_once "include/scripts.php"; ?>
</html>