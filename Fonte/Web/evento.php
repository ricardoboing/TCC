<!DOCTYPE html>
<html>
<?php include "class/ClienteServer.php"; ?>
<?php include_once "include/head.php"; ?>
<?php
	$id = $_GET["id"];

	if ($id == "") {
		$title = "NOVO EVENTO";

		$nome = "";
		$somTocar = "";
		$somVolume = "50";
		$somTempoDuracao = "";

		$semanaDomingo = "";
		$semanaSegunda = "";
		$semanaTerca   = "";
		$semanaQuarta  = "";
		$semanaQuinta  = "";
		$semanaSexta   = "";
		$semanaSabado  = "";

		$horarioHora   = "";
		$horarioMinuto = "";
	} else {
		$title = "EDITAR EVENTO";

		$pacote = "f";

		$clienteServer = new ClienteServer();
		$clienteServer->criarConexao();
		$clienteServer->conectar();
		$clienteServer->enviar($pacote);
		
		$subPacote1 = $clienteServer->ler(12); //"00000001234212";

		echo "\"".$subPacote1."\"<br>"; // 00000009542217
		
		/*
		$nome = "";
		$somTocar = (substr($subPacote1, -,1) == "0")? "" : " checked";
		$somVolume = substr($subPacote1, , 3);
		$somTempoDuracao = substr($subPacote1, , 2);
		*/
		
		$semanaDomingo = (substr($subPacote1, 0, 1) == "0")? "" : " checked";
		$semanaSegunda = (substr($subPacote1, 1, 1) == "0")? "" : " checked";
		$semanaTerca   = (substr($subPacote1, 2, 1) == "0")? "" : " checked";
		$semanaQuarta  = (substr($subPacote1, 3, 1) == "0")? "" : " checked";
		$semanaQuinta  = (substr($subPacote1, 4, 1) == "0")? "" : " checked";
		$semanaSexta   = (substr($subPacote1, 5, 1) == "0")? "" : " checked";
		$semanaSabado  = (substr($subPacote1, 6, 1) == "0")? "" : " checked";

		$horarioHora   = substr($subPacote1, 7, 2);
		$horarioMinuto = substr($subPacote1, 9, 2);

		$clienteServer->desconectar();
	}
?>

<body>
	<header>
		<span><?php echo $title; ?></span>
	</header>
	<main class="evento">
		<form>
			<section class="evento">
				<div>
					<label for="nome">Nome:</label>
					<input type="text" name="nome" id="nome" placeholder="De manhã" required="required" value=<?php echo $nome; ?>>
				</div>
				<div class="hora">
					<label for="horario_hora">Horário:</label>
					<div>
						<input type="text" class="number" name="horario_minuto" id="horario_minuto" placeholder="00" required="required" value=<?php echo "\"".$horarioHora."\""; ?>>
						<div>
							<span>:</span>
						</div>
						<input type="text" class="number" name="horario_hora" id="horario_hora" placeholder="01" required="required" value=<?php echo "\"".$horarioMinuto."\""; ?>>
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
					<input type="checkbox" name="som_input_checkbox" id="som_input_checkbox">
				</div>
				<div>
					<label for="som_input_volume">Volume:</label>
					<input type="range" name="som_input_volume" id="som_input_volume" disabled="disabled">
				</div>
				<div class="tempo">
					<label for="som_input_tempo">Tempo:</label>
					<div>
						<input type="text" class="number" name="som_input_tempo" id="som_input_tempo" placeholder="0" disabled="disabled">
						<span class="disabled">segundos</span>
					</div>
				</div>
			</section>
		</form>
	</main>
	<footer>
		<ul>
			<li>
				<a href="javascript: void(0);" class="salvar" data-href="eventos.php">SALVAR</a>
			</li>
			<li>
				<a href="eventos.php" class="cancelar">CANCELAR</a>
			</li>
		</ul>
	</footer>
</body>
<?php include_once "include/scripts.php"; ?>
</html>