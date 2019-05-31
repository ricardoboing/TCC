<!DOCTYPE html>
<html>
<?php include_once "class/ClienteServer.php"; ?>
<?php include_once "include/head.php"; ?>
<body>
	<header>
		<span>CONTROLE</span>
	</header>
	<main class="controle">
		<section class="iot_movimentacao">
			<div class="titulo">
				<span>IOT</span>
			</div>
			
			<div class="botoes">
				<ul>
					<li>
						<button id="iot_ativar" class="ativar">ATIVAR</button>
					</li>
				</ul>
			</div>
		</section>
		<section class="som">
			<div class="titulo">
				<span>Som</span>
			</div>
			<div class="botoes">
				<ul>
					<li>
						<button id="som_tocar" class="tocar">TOCAR</button>
					</li>
					<li>
						<button id="som_parar" class="parar">PARAR</button>
					</li>
				</ul>
			</div>
			<div>
				<label for="som_volume">Volume:</label>
				<input type="range" id="som_volume" value="100">
			</div>
		</section>
	</main>
	<footer>
		<ul>
			<!--<li>
				<a href="index.php">INÍCIO</a>
			</li>-->
			<li data-active="active">
				<a href="javascript: void(0);">CONTROLE</a>
			</li>
			<li>
				<a href="agenda.php">AGENDA</a>
			</li>
			<!--<li>
				<a href="configuracoes.php?page=controle">CONFIG.</a>
			</li>-->
		</ul>
	</footer>
</body>
<?php include_once "include/scripts.php"; ?>
</html>