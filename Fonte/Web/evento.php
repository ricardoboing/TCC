<!DOCTYPE html>
<html>
<?php include_once "class/ClienteServer.php"; ?>
<?php include_once "include/head.php"; ?>
<?php include_once "util/util.php"; ?>
<?php
	$id = $_GET["id"];

	$tipoDaPagina = "insert";
	$title = "NOVO AGENDAMENTO";

	$semanaDomingo = "";
	$semanaSegunda = "";
	$semanaTerca   = "";
	$semanaQuarta  = "";
	$semanaQuinta  = "";
	$semanaSexta   = "";
	$semanaSabado  = "";

	$horarioHora   = "";
	$horarioMinuto = "";

	$nome = "";
	$somTocar = "";
	$somVolume = "50";
	$somTempoDuracao = "00";
	$somDisabled = "disabled='disabled'";

	if ($id != "") {
		$tipoDaPagina = "update";
		$title = "EDITAR AGENDAMENTO";

		$pacote = "d";
		$pacote .= formatar_digitos($id, 10, "0");

		$clienteServer = new ClienteServer();
		$clienteServer->criarConexao();
		$clienteServer->conectar();
		$clienteServer->enviar($pacote);
		
		$semanaDomingo = ($clienteServer->ler(1) == "0")? "" : " checked=\"checked\"";
		$semanaSegunda = ($clienteServer->ler(1) == "0")? "" : " checked=\"checked\"";
		$semanaTerca   = ($clienteServer->ler(1) == "0")? "" : " checked=\"checked\"";
		$semanaQuarta  = ($clienteServer->ler(1) == "0")? "" : " checked=\"checked\"";
		$semanaQuinta  = ($clienteServer->ler(1) == "0")? "" : " checked=\"checked\"";
		$semanaSexta   = ($clienteServer->ler(1) == "0")? "" : " checked=\"checked\"";
		$semanaSabado  = ($clienteServer->ler(1) == "0")? "" : " checked=\"checked\"";

		$horarioHora   = $clienteServer->ler(2)."";
		$horarioMinuto = $clienteServer->ler(2)."";

		$somTocar = $clienteServer->ler(1)."";
		if ($somTocar == "1") {
			$somVolume = $clienteServer->ler(3);
			$somTempoDuracao = $clienteServer->ler(2);
			$somTocar = "checked=\"checked\"";
			$somDisabled = "";
		} else {
			$somTocar = "";
		}

		$lengthNome = $clienteServer->ler(2);
		$nome = $clienteServer->ler($lengthNome);

		$clienteServer->desconectar();
	}
?>
<body>
	<header>
		<span><?php echo $title; ?></span>
	</header>
	<main class="evento" data-operacao=<?php echo "'".$tipoDaPagina."'"; ?> data-id=<?php echo "'".$id."'"; ?>>
		<form>
			<section class="evento">
				<div>
					<label for="nome">Nome:</label>
					<input type="text" name="nome" id="nome" placeholder="De manha" required="required" value=<?php echo "'".$nome."'"; ?>>
				</div>
				<div class="hora">
					<label for="horario_hora">Horário:</label>
					<div>
						<input type="text" class="number" name="horario_minuto" id="horario_minuto" placeholder="00" required="required" value=<?php echo "\"".$horarioMinuto."\""; ?>>
						<div>
							<span>:</span>
						</div>
						<input type="text" class="number" name="horario_hora" id="horario_hora" placeholder="01" required="required" value=<?php echo "\"".$horarioHora."\""; ?>>
					</div>
				</div>
				<div>
					<ul>
						<li>
							<label for="dia_domingo">Domingo</label>
							<input type="checkbox" name="dia_domingo" id="dia_domingo" <?php echo $semanaDomingo; ?>>
						</li>
						<li>
							<label for="dia_segunda">Segunda</label>
							<input type="checkbox" name="dia_segunda" id="dia_segunda" <?php echo $semanaSegunda; ?>>
						</li>
						<li>
							<label for="dia_terca">Terça</label>
							<input type="checkbox" name="dia_terca" id="dia_terca" <?php echo $semanaTerca; ?>>
						</li>
						<li>
							<label for="dia_quarta">Quarta</label>
							<input type="checkbox" name="dia_quarta" id="dia_quarta" <?php echo $semanaQuarta; ?>>
						</li>
						<li>
							<label for="dia_quinta">Quinta</label>
							<input type="checkbox" name="dia_quinta" id="dia_quinta" <?php echo $semanaQuinta; ?>>
						</li>
						<li>
							<label for="dia_sexta">Sexta</label>
							<input type="checkbox" name="dia_sexta" id="dia_sexta" <?php echo $semanaSexta; ?>>
						</li>
						<li>
							<label for="dia_sabado">Sábado</label>
							<input type="checkbox" name="dia_sabado" id="dia_sabado" <?php echo $semanaSabado; ?>>
						</li>
					</ul>
				</div>
			</section>
			<section class="som">
				<div class="titulo">
					<span>Som</span>
				</div>
				<div>
					<label for="som_input_checkbox">Tocar:</label>
					<input type="checkbox" name="som_input_checkbox" id="som_input_checkbox" <?php echo $somTocar; ?>>
				</div>
				<div>
					<label for="som_input_volume">Volume:</label>
					<input type="range" name="som_input_volume" id="som_input_volume" value=<?php echo "'".$somVolume."'"; ?> <?php echo $somDisabled; ?>>
				</div>
				<div class="tempo">
					<label for="som_input_tempo">Tempo:</label>
					<div>
						<input type="text" class="number" name="som_input_tempo" id="som_input_tempo" placeholder="0" value=<?php echo "'".$somTempoDuracao."'"; ?> <?php echo $somDisabled; ?>>
						<span class="disabled">segundos</span>
					</div>
				</div>
			</section>
		</form>
	</main>
	<footer>
		<ul>
			<li>
				<a href="javascript: void(0);" class="salvar" data-href="agenda.php">SALVAR</a>
			</li>
			<li>
				<a href="agenda.php" class="cancelar">CANCELAR</a>
			</li>
		</ul>
	</footer>
</body>
<?php include_once "include/scripts.php"; ?>
</html>