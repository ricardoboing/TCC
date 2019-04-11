<!DOCTYPE html>
<html>
<?php include_once "include/head.php"; ?>
<body>
	<header>
		<span>HORÁRIOS</span>
	</header>
	<main class="lista_de_evento">
		<section>
			<table>
				<tr data-id="1">
					<td class="horario">
						<span>07:15</span>
					</td>
					<td class="nome">
						<a href="evento.html">Evento</a>
						<ul>
							<li>
								<span>D</span>
							</li>
							<li class="bold">
								<span>S</span>
							</li>
							<li>
								<span>T</span>
							</li>
							<li class="bold">
								<span>Q</span>
							</li>
							<li>
								<span>Q</span>
							</li>
							<li class="bold">
								<span>S</span>
							</li>
							<li>
								<span>S</span>
							</li>
						</ul>
					</td>
					<td class="status">
						<input type="checkbox">
					</td>
				</tr>
				<tr data-id="2">
					<td class="horario">
						<span>08:20</span>
					</td>
					<td class="nome">
						<a href="evento.html">Evento</a>
						<ul>
							<li>
								<span>D</span>
							</li>
							<li>
								<span>S</span>
							</li>
							<li class="bold">
								<span>T</span>
							</li>
							<li>
								<span>Q</span>
							</li>
							<li class="bold">
								<span>Q</span>
							</li>
							<li>
								<span>S</span>
							</li>
							<li>
								<span>S</span>
							</li>
						</ul>
					</td>
					<td class="status">
						<input type="checkbox">
					</td>
				</tr>
				<tr data-id="3">
					<td class="horario">
						<span>10:00</span>
					</td>
					<td class="nome">
						<a href="evento.html">Evento</a>
						<ul>
							<li class="bold">
								<span>D</span>
							</li>
							<li class="bold">
								<span>S</span>
							</li>
							<li class="bold">
								<span>T</span>
							</li>
							<li class="bold">
								<span>Q</span>
							</li>
							<li class="bold">
								<span>Q</span>
							</li>
							<li class="bold">
								<span>S</span>
							</li>
							<li class="bold">
								<span>S</span>
							</li>
						</ul>
					</td>
					<td class="status">
						<input type="checkbox">
					</td>
				</tr>
				<tr data-id="4">
					<td class="horario">
						<span>09:30</span>
					</td>
					<td class="nome">
						<a href="evento.html">Evento</a>
						<ul>
							<li>
								<span>D</span>
							</li>
							<li>
								<span>S</span>
							</li>
							<li>
								<span>T</span>
							</li>
							<li>
								<span>Q</span>
							</li>
							<li>
								<span>Q</span>
							</li>
							<li class="bold">
								<span>S</span>
							</li>
							<li>
								<span>S</span>
							</li>
						</ul>
					</td>
					<td class="status">
						<input type="checkbox">
					</td>
				</tr>
				<tr data-id="5">
					<td class="horario">
						<span>08:15</span>
					</td>
					<td class="nome">
						<a href="evento.html">Evento</a>
						<ul>
							<li class="bold">
								<span>D</span>
							</li>
							<li>
								<span>S</span>
							</li>
							<li>
								<span>T</span>
							</li>
							<li>
								<span>Q</span>
							</li>
							<li>
								<span>Q</span>
							</li>
							<li>
								<span>S</span>
							</li>
							<li class="bold">
								<span>S</span>
							</li>
						</ul>
					</td>
					<td class="status">
						<input type="checkbox">
					</td>
				</tr>
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