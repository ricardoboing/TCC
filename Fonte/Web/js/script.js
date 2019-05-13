$(document).ready(function() {
	var main = $("main")[0];
	var pagina = $(main).attr("class");
	
	switch (pagina) {
		case "estimativa_de_consumo":
			page_estimativa_de_consumo();
			break;
		case "evento":
			page_evento();
			break;
		case "lista_de_evento":
			page_lista_de_evento();
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

	console.log(url+data);

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

const message_box_type = {
	SUCESS: 0,
	ERROR: 1,
	FAIL: 2
};
// Futuramente implementar algo melhor (nao usar esse alert padrao)
function message_box(box_type, message) {
	switch(box_type) {
		case message_box_type.SUCESS:
			alert("SUCESSO\n"+message);
			break;
		case message_box_type.ERROR:
			alert("ERRO\n"+message);
			break;
		case message_box_type.FAIL:
			alert("OPERAÇÃO FALHOU\n"+message);
			break;
		default:
			break;
	}
}

/* --------------------- [Class] FrontIndexTarifa --------------------- */
class FrontEstimativaDeConsumo {
	static recalcularEstimativaDeConsumo() {
		var valorDaTarifa = parseInt($($("table#tarifa input")[0]).val());

		// [TABLE] Consumo_Carrinho
		FrontEstimativaDeConsumo.recalcularEstimativaDeConsumoDaTable(
			$("table#table_consumo_carrinho"),
			valorDaTarifa
		);
		// [TABLE] Consumo_Fog
		FrontEstimativaDeConsumo.recalcularEstimativaDeConsumoDaTable(
			$("table#table_consumo_fog"),
			valorDaTarifa
		);
		// [TABLE] Consumo_Total_Completo
		FrontEstimativaDeConsumo.recalcularEstimativaDeConsumoDaTable(
			$("table#table_consumo_total"),
			valorDaTarifa
		);
	}
	static recalcularEstimativaDeConsumoDaTable(table, valorDaTarifa) {
		if ( $(table).attr("id") == "table_consumo_total" ) {
			var tdValorFinanceiro, tdConsumoFog, tdConsumoCarrinho;
			var consumoFog, consumoCarrinho;

			// [TABLE] Consumo_Total_Completo
			tdValorFinanceiro = $(table).find("tr.valor_financeiro td span");
			tdConsumoFog = $("table#table_consumo_fog tr.valor_financeiro td span");
			tdConsumoCarrinho = $("table#table_consumo_carrinho tr.valor_financeiro td span");

			// Dia
			consumoFog = parseFloat($($(tdConsumoFog)[0]).text());
			consumoCarrinho = parseFloat($($(tdConsumoCarrinho)[0]).text());
			$($(tdValorFinanceiro)[0]).text(consumoFog + consumoCarrinho);
			
			// Mes
			consumoFog = parseFloat($($(tdConsumoFog)[1]).text());
			consumoCarrinho = parseFloat($($(tdConsumoCarrinho)[1]).text());
			$($(tdValorFinanceiro)[1]).text(consumoFog + consumoCarrinho);
			
			// Ano
			consumoFog = parseFloat($($(tdConsumoFog)[2]).text());
			consumoCarrinho = parseFloat($($(tdConsumoCarrinho)[2]).text());
			$($(tdValorFinanceiro)[2]).text(consumoFog + consumoCarrinho);
		} else {
			var tdTempoDeConsumo, tdValorFinanceiro, tdConsumoWatt;
			var consumo, tempo;

			// [TABLE] Consumo_Total_Completo
			tdValorFinanceiro = $(table).find("tr.valor_financeiro td span");
			tdTempoDeConsumo = $(table).find("tr.tempo td span");
			tdConsumoWatt = $(table).find("tr.consumo td span");

			// Dia
			consumo = parseFloat($($(tdConsumoWatt)[0]).text());
			tempo = parseFloat($($(tdTempoDeConsumo)[0]).text());
			$($(tdValorFinanceiro)[0]).text(consumo * tempo * valorDaTarifa);
			
			// Mes
			consumo = parseFloat($($(tdConsumoWatt)[1]).text());
			tempo = parseFloat($($(tdTempoDeConsumo)[1]).text());
			$($(tdValorFinanceiro)[1]).text(consumo * tempo * valorDaTarifa);
			
			// Ano
			consumo = parseFloat($($(tdConsumoWatt)[2]).text());
			tempo = parseFloat($($(tdTempoDeConsumo)[2]).text());
			$($(tdValorFinanceiro)[2]).text(consumo * tempo * valorDaTarifa);
		}
	}
	static salvarTarifa(button) {
		var trTarifa = $(button).parents("tr")[0];

		function function_sucess(data) {
			message_box(
				message_box_type.SUCESS,
				"Salvo com sucesso!"
			);
			FrontEstimativaDeConsumo.recalcularEstimativaDeConsumo();
		}
		function function_error(data) {
			message_box(
				message_box_type.FAIL,
				"Algo inesperado ocorreu no servidor.\nVerifique a corretude dos dados e tente mais tarde."
			);
		}

		BackEstimativaDeConsumo.salvarTarifa($(trTarifa), function_sucess, function_error);
	}
};
class BackEstimativaDeConsumo {
	static salvarTarifa(trTarifa, front_function_sucess, front_function_error) {
		var valorCobrado = $($(trTarifa).find("td input")[0]).val();
		
		function function_sucess(data) {
			console.log("Sucess:");
			console.log(data);

			if (data) {
				front_function_sucess(data);
			} else {
				front_function_error(data);
			}
		}
		function function_error(data) {
			front_function_error(data);
		}

		Ajax("action/estimativa_de_consumo/tarifa/update.php", "valor="+valorCobrado, function_sucess, function_error);
	}
}

/* --------------------- [FunctionPage] Index --------------------- */
function page_estimativa_de_consumo() {
	$("table#tarifa button").click(function() {
		FrontEstimativaDeConsumo.salvarTarifa($(this));
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
	static salvar(button) {
		var nome = $("#nome").val();

		if (nome == "" || nome == undefined) {
			message_box(
				message_box_type.ERROR,
				"Insira um nome para o evento."
			);
			return;
		}

		function function_sucess(data) {
			message_box(
				message_box_type.SUCESS,
				"Salvo com sucesso!"
			);
			$(window.document.location).attr("href", $(button).attr("data-href"));
		}
		function function_error(data) {
			message_box(
				message_box_type.FAIL,
				"Algo inesperado ocorreu no servidor.\nVerifique a corretude dos dados e tente mais tarde."
			);
		}

		BackEvento.salvar(function_sucess, function_error);
	}
}
class BackEvento {
	static salvar(front_function_sucess, front_function_error) {
		// Dados gerais
		var nome = $("#nome").val();
		var horario = "";
		
		var horarioHora = $("#horario_hora").val()+"";
		if (horarioHora.length < 2) {
			horario += "0" +horarioHora;
		} else {
			horario += horarioHora.substring(0,2);
		}

		var horarioMinuto = $("#horario_minuto").val() +"";
		if (horarioMinuto.length < 2) {
			horario += "0" +horarioMinuto;
		} else {
			horario += horarioMinuto.substring(0,2);
		}

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

		function function_sucess(data) {
			console.log("Sucess:");
			console.log(data);

			if (data) {
				front_function_sucess(data);
			} else {
				front_function_error(data);
			}
		}
		function function_error(data) {
			console.log(data);
			front_function_error(data);
		}

		var operacaoASerRealizada = $($("main").get(0)).attr("data-operacao");
		var urlDaPagina = "insert";

		if (operacaoASerRealizada == "update") {
			urlDaPagina = "update";

			var id = $($("main").get(0)).attr("data-id");
			dado += "&id="+id;
		}

		Ajax("action/evento/"+urlDaPagina+".php", dado, function_sucess, function_error);
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
		FrontEvento.salvar($(this));
	});
}

/* --------------------- [Class] ListaDeEvento --------------------- */
class FrontListaDeEvento {
	static select() {
		console.log("oi");
		var arrayCheckbox = $("table input:checkbox:checked");
		console.log(arrayCheckbox);
		console.log($(arrayCheckbox));

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
		var dataId = "";

		for (var c = 0; c < $(arrayTr).length; c++) {
			var tr = $(arrayTr)[c];
			
			if ($(tr).find("input").prop("checked")) {
				if (dataId != "") {
					dataId += ",";
				}
				dataId += $(tr).attr("data-id");
			}
		}

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

			FrontListaDeEvento.select();
		}
		function function_error(data) {
			message_box(
				message_box_type.FAIL,
				"Algo inesperado ocorreu no servidor. Tente mais tarde."
			);

			$("input:checkbox").prop("disabled", false);
		}

		BackListaDeEvento.remove(dataId, function_sucess, function_error);
	}
	static insert() {
		var button = $("input#insert_event");
		$(window.document.location).attr("href", $(button).attr("data-href"));
	}
}
class BackListaDeEvento {
	static remove(dataId, front_function_sucess, front_function_error) {
		function function_sucess(data) {
			console.log("Sucess:");
			console.log(data);

			if (data) {
				front_function_sucess(data);
			} else {
				front_function_error(data);
			}
		}
		function function_error(data) {
			front_function_error(data);
		}

		Ajax("action/evento/remove.php", "id="+dataId, function_sucess, function_error);
	}
}

/* --------------------- [FunctionPage] Horarios --------------------- */
function page_lista_de_evento() {
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
