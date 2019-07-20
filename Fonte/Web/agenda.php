<!DOCTYPE html>
<html>
<?php
header("Content-type: text/html;charset=utf-8");
include_once "class/ClienteServer.php";
include_once "include/head.php";
?>

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
					$numeroDeAgendamentos = intval($clienteServer->ler(3));
					for ($c = 0; $c < $numeroDeAgendamentos; $c++) {
						$id = $clienteServer->ler(10);
						
						if ($id == "") {
							break;
						}
						
						$id = intval($id);

						$semanaDomingo = ($clienteServer->ler(1) == "0")? "" : " class=\"bold\"";
						$semanaSegunda = ($clienteServer->ler(1) == "0")? "" : " class=\"bold\"";
						$semanaTerca   = ($clienteServer->ler(1) == "0")? "" : " class=\"bold\"";
						$semanaQuarta  = ($clienteServer->ler(1) == "0")? "" : " class=\"bold\"";
						$semanaQuinta  = ($clienteServer->ler(1) == "0")? "" : " class=\"bold\"";
						$semanaSexta   = ($clienteServer->ler(1) == "0")? "" : " class=\"bold\"";
						$semanaSabado  = ($clienteServer->ler(1) == "0")? "" : " class=\"bold\"";

						$horarioHora   = $clienteServer->ler(2);
						$horarioMinuto = $clienteServer->ler(2);
						$horario = $horarioHora.":".$horarioMinuto;

						$lengthNome = intval($clienteServer->ler(2));

						$nome = $clienteServer->ler($lengthNome);
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
				<a href="index.php">CONTROLE</a>
			</li>
			<li data-active="active">
				<a href="javascript: void(0);">AGENDA</a>
			</li>
		</ul>
	</footer>
</body>
<?php include_once "include/scripts.php"; ?>
</html>