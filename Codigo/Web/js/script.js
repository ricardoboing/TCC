$(document).ready(function() {
	var main = $("main")[0];
	var pagina = $(main).attr("class");
	
	switch (pagina) {
		case "index":
			page_index();
			console.log("INDEX");
			break;
		case "evento":
			page_evento();
			console.log("EVENTO")
			break;
		case "horarios":
			page_horarios();
			console.log("HORARIOS")
			break;
		default:
			break;
	}
});
function Ajax(url, data, function_sucess, function_error) {
	if (data != undefined && data != "") {
		data = "?"+data;
	} else {
		data = "";
	}

	$.ajax({
		url: url+data,
		dataType: "json",
		contentType: "application/json; charset=utf-8",
		success: function(d) {
			function_sucess(d);
		},
		type: 'GET',
		error: function(d) {
			function_error(d);
		}
	});
}

/* --------------------- [Class] FrontIndexTarifa --------------------- */
class FrontIndexTarifa {
	static adicionarTarifa(button) {
		var trMenu = $(button).parents("tr.menu")[0];
		var table = $(button).parents("table")[0];
		
		var trClonada = $(table).find("tr")[1];
		var trClone = $(trClonada).clone();

		$(trMenu).remove();
		$(trClonada).parent().append(trClone);
		$(trClonada).parent().append(trMenu);

		$(trClone).attr("data-id", "-1");
		$(trClone).find("button.remover").click(function() {
			FrontIndexTarifa.removerTarifa($(this));
		});
		$(trMenu).find("button.adicionar").click(function() {
			FrontIndexTarifa.adicionarTarifa($(this));
		});

		// Habilita remocao de tarifas (desativada quando existir apenas uma tarifa)
		$(table).find("button.remover").prop("disabled", false);
	}
	static removerTarifa(button) {
		var trPai = $(button).parents("tr")[0];
		var elementoAvo = $(trPai).parent();

		var numeroFilhosDoAvo = $(elementoAvo).find("tr").length;

		// Se o "avo" do elemento possuir duas ou menos tr
		if (numeroFilhosDoAvo <= 3) {
			return;
		}

		function function_sucess(data) {
			$(trPai).remove();

			// Desabilita remocao de tarifas quando existir apenas uma
			if (numeroFilhosDoAvo <= 4) { // 4 tr: cabecalho; 2x tarifa; buttons
				var ultimaTrDeTarifa = $(elementoAvo).find("tr")[1];
				$(ultimaTrDeTarifa).find("button.remover").prop("disabled", true);
			}
		}
		function function_error(data) {

		}

		BackIndexFarifa.removerTarifa($(trPai), function_sucess, function_error);
	}
};
class BackIndexFarifa {
	static removerTarifa(trTarifa, front_function_sucess, front_function_error) {
		var url = "action/estimativa_de_consumo/tarifa/";
		
		var tdTarifaValor = $(trTarifa).find("input")[0];
		var tdTarifaConsumo = $(trTarifa).find("input")[1]

		var dataId = $(trTarifa).attr("data-id");
		var valor = $(tdTarifaValor).val();
		var consumo = $(tdTarifaConsumo).val();

		var data = "valor="+valor+"&consumo="+consumo;

		// Ainda nao foi efetivamente salva: adiciona nova tarifa
		if (dataId == "-1") {
			url += "insert.php";
		}
		// Senao: atualiza tarifa existente
		else {
			url += "update.php";
			data += "&id="+dataId;
		}

		function function_sucess(data) {
			console.log("Sucess:");
			console.log(data);
			front_function_sucess(data);
		}
		function function_error(data) {
			console.log("Error:");
			console.log(data);
			front_function_error(data);
		}

		Ajax(url, data, function_sucess, function_error);
	}
	static salvarTarifa(trTarifa, front_function_sucess, front_function_error) {
		var dataId = $(trTarifa).attr("data-id");

		// Ainda nao foi efetivamente salva: nao se comunica com o servidor
		if (dataId == "-1") {
			front_function_sucess();
			return;
		}

		function function_sucess(data) {
			console.log("Sucess:");
			console.log(data);
			front_function_sucess(data);
		}
		function function_error(data) {
			console.log("Error:");
			console.log(data);
			front_function_error(data);
		}

		Ajax("action/estimativa_de_consumo/tarifa/remove.php", "id="+dataId, function_sucess, function_error);
	}
}

/* --------------------- [FunctionPage] Index --------------------- */
function page_index() {
	$("table.tarifa button.remover").click(function() {
		FrontIndexTarifa.removerTarifa($(this));
	});
	$("table.tarifa button.adicionar").click(function() {
		FrontIndexTarifa.adicionarTarifa($(this));
	});
}

/* --------------------- [Class] ManualCarrinho --------------------- */
var DIRECAO = {
	PARADO: 0,
	ANDAR_ESQUERDA: 1,
	ANDAR_DIREITA: 2
};
var ManualCarrinho = function() {
	this.direcao = DIRECAO.PARADO;
	this.velocidade = 0;
};
ManualCarrinho.prototype.andar_esquerda = function() {
	console.log("ANDAR_ESQUERDA");
};
ManualCarrinho.prototype.andar_direita = function() {
	console.log("ANDAR_DIREITA");
};
ManualCarrinho.prototype.parar = function() {
	console.log("PARAR");
};
ManualCarrinho.prototype.set_velocidade = function(value) {
	console.log("SET_VELOCIDADE");
};

/* --------------------- [Class] ManualSom --------------------- */
var ManualSom = function() {
	this.parado = true;
	this.arquivo = "oie";
};
ManualSom.prototype.parar = function() {
	console.log("parar som");
};
ManualSom.prototype.tocar = function() {
	console.log("tocar som");
};
ManualSom.prototype.set_volume = function(value) {
	console.log("set_volume: "+value);
};
ManualSom.prototype.set_arquivo = function(value) {
	console.log("set_arquivo: "+value);	
};

/* --------------------- [FunctionPage] Index --------------------- */
function page_manual() {
	var carrinho = new IndexCarrinho();
	$("#carrinho_button_direita").click(function() {
		carrinho.andar_direita();
	});
	$("#carrinho_button_esquerda").click(function() {
		carrinho.andar_esquerda();
	});
	$("#carrinho_button_parar").click(function() {
		carrinho.parar();
	});
	$("#carrinho_input_velocidade").mouseup(function() {
		var value = $(this).val();
		carrinho.set_velocidade(value);
	});

	var som = new IndexSom();
	$("#som_button_tocar").click(function() {
		som.tocar();
	});
	$("#som_button_parar").click(function() {
		som.parar();
	});
	$("#som_input_volume").mouseup(function() {
		var value = $(this).val();
		som.set_volume(value);
	});
	$("#som_input_arquivo").mouseup(function() {
		var value = $(this).val();
		console.log(value);
		alert("Após selecionar o arquivo de áudio, clique novamente em \"Tocar\"!");
	});
}

/* --------------------- [Class] EventoSom --------------------- */
class FrontEvento {
	static ativarSom() {
		$("#som_input_tempo").prop("disabled", false);
		$("#som_input_volume").prop("disabled", false);
		$("#som_input_arquivo").prop("disabled", false);

		$("#som_input_tempo").prop("required", true);
		$("#som_input_volume").prop("required", true);
		$("#som_input_arquivo").prop("required", true);
		console.log("ativar");
	}
	static desativarSom() {
		$("#som_input_tempo").prop("disabled", true);
		$("#som_input_volume").prop("disabled", true);
		$("#som_input_arquivo").prop("disabled", true);

		$("#som_input_tempo").prop("required", false);
		$("#som_input_volume").prop("required", false);
		$("#som_input_arquivo").prop("required", false);
		console.log("desativar");
	}
	static salvar() {
		var nome = $("#nome").val();

		if (nome == "" || nome == undefined) {
			return;
		}

		function function_sucess(data) {
			$(window.document.location).attr("href", "horarios.html");
		}
		function function_error(data) {
			console.log("Error:");
			console.log(data);
		}

		BackEvento.salvar(function_sucess, function_error);
	}
	static cancelar() {
		$(window.document.location).attr("href", "horarios.html");
	}
}
class BackEvento {
	static salvar(front_function_sucess, front_function_error) {
		// Dados gerais
		var nome = $("#nome").val();
		var horario = $("#horario_hora").val() + ":" + $("#horario_minuto").val();
		
		var segunda = $("#dia_segunda").prop("checked");
		var terca = $("#dia_terca").prop("checked");
		var quarta = $("#dia_quarta").prop("checked");
		var quinta = $("#dia_quinta").prop("checked");
		var sexta = $("#dia_sexta").prop("checked");
		var sabado = $("#dia_sabado").prop("checked");
		var domingo = $("#dia_domingo").prop("checked");

		// Dados do som
		var somTocar = $("#som_input_checkbox").prop("checked");
		var somVolume = $("#som_input_volume").val();
		var somTempo = $("#som_input_tempo").val();

		// String dados
		var dado = "nome=" + nome;
		dado += "&horario=" + horario;
		dado += "&segunda=" + (segunda? "1" : "0");
		dado += "&terca=" + (terca? "1" : "0");
		dado += "&quarta=" + (quarta? "1" : "0");
		dado += "&quinta=" + (quinta? "1" : "0");
		dado += "&sexta=" + (sexta? "1" : "0");
		dado += "&sabado=" + (sabado? "1" : "0");
		dado += "&domingo=" + (domingo? "1" : "0");

		dado += "&somTocar=" + (somTocar? "1" : "0");
		dado += "&somVolume=" + somVolume;
		dado += "&somTempo=" + somTempo;

		console.log(dado);

		Ajax("action/evento/insert.php", dado, front_function_sucess, front_function_error);
	}
}

/* --------------------- [FunctionPage] Evento --------------------- */
function page_evento() {
	$("#som_input_checkbox").change(function() {
		var checked = $(this).prop("checked");
		console.log(checked);

		if (checked) {
			FrontEvento.ativarSom();
		} else {
			FrontEvento.desativarSom();
		}
	});
	$("footer a.salvar").click(function() {
		FrontEvento.salvar();
	});
	$("footer a.cancelar").click(function() {
		FrontEvento.cancelar();
	});
}

/* --------------------- [Class]  --------------------- */
class FrontListaDeEvento {
	static select() {
		var arrayCheckbox = $("table input:checkbox:checked");
		
		if ($(arrayCheckbox).length <= 0) {
			$("input.remove:button").attr("data-disabled", "disabled");
			$("input.insert:button").attr("data-disabled", "enabled");
		} else {
			$("input.remove:button").attr("data-disabled", "enabled");
			$("input.insert:button").attr("data-disabled", "disabled");
		}
	}
	static remove(arrayTr) {
		$("input:checkbox").prop("disabled", true);

		function function_sucess(data) {
			console.log("Sucess:");
			console.log(data);

			$("input:checkbox").prop("disabled", false);

			for (var c = 0; c < $(arrayTr).length; c++) {
				var tr = $(arrayTr)[c];
				
				if ($(tr).find("input").prop("checked")) {
					$(tr).remove();
				}
			}
		}
		function function_error(data) {
			console.log("Error:");
			console.log(data);
			$("input:checkbox").prop("disabled", false);
		}

		BackListaDeEvento.remove(arrayTr, function_sucess, function_error);
	}
	static insert() {
		$(window.document.location).attr("href", "evento.html");
	}
}
class BackListaDeEvento {
	static remove(arrayTr, front_function_sucess, front_function_error) {
		var id = "";
		for (var c = 0; c < $(arrayTr).length; c++) {
			var tr = $(arrayTr)[c];
			var dataId = $(tr).attr("data-id");

			if (c > 0) {
				id += ",";
			}
			id += dataId;
		}

		Ajax("action/evento/remove.php", "id="+id, front_function_sucess, front_function_error);
	}
}

/* --------------------- [FunctionPage] Horarios --------------------- */
function page_horarios() {
	$("table input:checkbox").click(function() {
		console.log("active checkbox");
		var tr = $(this).parents("tr")[0];
		
		FrontListaDeEvento.select(tr);
	});
	$("input.insert:button").click(function() {
		FrontListaDeEvento.insert();
	});
	$("input.remove:button").click(function() {
		var arrayTr = $("table tr");
		FrontListaDeEvento.remove(arrayTr);
	});
}
