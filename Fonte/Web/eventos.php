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
?>
<body>
	<header>
		<span>HORÁRIOS</span>
	</header>
	<main class="lista_de_evento">
		<section>
			<table>
				<?php
					while (true) {
						$subPacote1 = $clienteServer->ler(15);
						
						if ($subPacote1 == "") {
							break;
						}
						//echo "\"".$subPacote1."\"";
						$semanaDomingo = (substr($subPacote1, 0, 1) == "0")? "" : " class=\"bold\"";
						$semanaSegunda = (substr($subPacote1, 1, 1) == "0")? "" : " class=\"bold\"";
						$semanaTerca   = (substr($subPacote1, 2, 1) == "0")? "" : " class=\"bold\"";
						$semanaQuarta  = (substr($subPacote1, 3, 1) == "0")? "" : " class=\"bold\"";
						$semanaQuinta  = (substr($subPacote1, 4, 1) == "0")? "" : " class=\"bold\"";
						$semanaSexta   = (substr($subPacote1, 5, 1) == "0")? "" : " class=\"bold\"";
						$semanaSabado  = (substr($subPacote1, 6, 1) == "0")? "" : " class=\"bold\"";

						$horarioHora   = substr($subPacote1, 7, 2);
						$horarioMinuto = substr($subPacote1, 9, 2);
						$horario = $horarioHora.":".$horarioMinuto;

						$digitosNome = substr($subPacote1, 11, 2);
						$digitosId = substr($subPacote1, 13, 2);

						$nome = $clienteServer->ler($digitosNome);
						$id = $clienteServer->ler($digitosId);
				?>
						<tr data-id=<?php echo "\"".$id."\""; ?>>
							<td class="horario">
								<span><?php echo $horario; ?></span>
							</td>
							<td class="nome">
								<a <?php echo "href='evento.php?id=".$id."'"; ?>><?php echo $nome; ?></a>
								<ul>
									<li <?php echo "\"".$semanaDomingo."\""; ?>>
										<span>D</span>
									</li>
									<li <?php echo "\"".$semanaSegunda."\""; ?>>
										<span>S</span>
									</li>
									<li <?php echo "\"".$semanaTerca."\""; ?>>
										<span>T</span>
									</li>
									<li <?php echo "\"".$semanaQuarta."\""; ?>>
										<span>Q</span>
									</li>
									<li <?php echo "\"".$semanaQuinta."\""; ?>>
										<span>Q</span>
									</li>
									<li <?php echo "\"".$semanaSexta."\""; ?>>
										<span>S</span>
									</li>
									<li <?php echo "\"".$semanaSabado."\""; ?>>
										<span>S</span>
									</li>
								</ul>
							</td>
							<td class="status">
								<input type="checkbox">
							</td>
						</tr>
				<?php
					}

					$clienteServer->desconectar();
				?>
			</table>
		</section>
	</main>
	<footer>
		<input type="button" id="insert_event" class="insert" value="+" data-disabled="enabled" data-href="evento.php">
		<input type="button" class="remove" value="-" data-disabled="disabled">
		<ul>
			<li>
				<a href="index.php">ESTIMATIVA DE CONSUMO</a>
			</li>
			<li>
				<a href="javascript: void(0);">HORÁRIOS</a>
			</li>
		</ul>
	</footer>
</body>
<?php include_once "include/scripts.php"; ?>
</html>