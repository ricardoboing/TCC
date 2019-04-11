<!DOCTYPE html>
<html>
<?php include_once "include/head.php"; ?>
<body>
	<header>
		<span>CRIAR EVENTO</span>
	</header>
	<main class="evento">
		<form>
			<section class="evento">
				<div>
					<label for="nome">Nome:</label>
					<input type="text" name="nome" id="nome" placeholder="De manhã" required="required">
				</div>
				<div class="hora">
					<label for="horario_hora">Horário:</label>
					<div>
						<input type="text" class="number" name="horario_minuto" id="horario_minuto" placeholder="00" required="required">
						<div>
							<span>:</span>
						</div>
						<input type="text" class="number" name="horario_hora" id="horario_hora" placeholder="01" required="required">
					</div>
				</div>
				<div>
					<ul>
						<li>
							<label for="dia_domingo">Domingo</label>
							<input type="checkbox" name="dia_domingo" id="dia_domingo">
						</li>
						<li>
							<label for="dia_segunda">Segunda</label>
							<input type="checkbox" name="dia_segunda" id="dia_segunda">
						</li>
						<li>
							<label for="dia_terca">Terça</label>
							<input type="checkbox" name="dia_terca" id="dia_terca">
						</li>
						<li>
							<label for="dia_quarta">Quarta</label>
							<input type="checkbox" name="dia_quarta" id="dia_quarta">
						</li>
						<li>
							<label for="dia_quinta">Quinta</label>
							<input type="checkbox" name="dia_quinta" id="dia_quinta">
						</li>
						<li>
							<label for="dia_sexta">Sexta</label>
							<input type="checkbox" name="dia_sexta" id="dia_sexta">
						</li>
						<li>
							<label for="dia_sabado">Sábado</label>
							<input type="checkbox" name="dia_sabado" id="dia_sabado">
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