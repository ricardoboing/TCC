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
		case "configuracoes":
			page_configuracoes();
			break;
		case "controle":
			page_controle();
			break;
		default:
			break;
	}

	$("footer li").click(function() {
		$(this).find("a")[0].click();
	});
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
	static reiniciarEstimativaDeConsumo() {
		function function_sucess(data) {
			message_box(
				message_box_type.SUCESS,
				"Tempo de duração da bateria\natualizado com sucesso!"
			);
		}
		function function_error(data) {
			message_box(
				message_box_type.FAIL,
				"Algo inesperado ocorreu no servidor.\nVerifique a corretude dos dados e tente mais tarde."
			);
		}

		BackEstimativaDeConsumo.reiniciarEstimativaDeConsumo(function_sucess, function_error);
	}
};
class BackEstimativaDeConsumo {
	static reiniciarEstimativaDeConsumo(front_function_sucess, front_function_error) {
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

		Ajax("action/estimativa_de_consumo/reiniciar_estimativa.php", "", function_sucess, function_error);
	}
}

/* --------------------- [FunctionPage] Index --------------------- */
function page_estimativa_de_consumo() {
	$("main button").click(function() {
		FrontEstimativaDeConsumo.reiniciarEstimativaDeConsumo($(this));
	});
}

/* --------------------- [Class] FrontConfiguracoes --------------------- */
class FrontConfiguracoes {
	static salvar(button) {
		var noIotTempoAtividade = $("#no_iot_tempo_atividade").val();

		if ($(button).prop("disabled") == true) {
			return;
		}

		if (noIotTempoAtividade == "" || noIotTempoAtividade == undefined) {
			message_box(
				message_box_type.ERROR,
				"Insira um tempo de atividade para o nó iot."
			);
			return;
		}

		var bateriaCapacidade = $("#bateria_capacidade").val();

		if (bateriaCapacidade == "" || bateriaCapacidade == undefined) {
			message_box(
				message_box_type.ERROR,
				"Insira a capacidade (corrente, em mA) da\nbateria utilizada no nó iot."
			);
			return;
		}

		

		function function_sucess(data) {
			message_box(
				message_box_type.SUCESS,
				"Salvo com sucesso!"
			);
			$(button).prop("disabled", false)
			$(window.document.location).attr("href", $(button).attr("data-href"));
		}
		function function_error(data) {
			message_box(
				message_box_type.FAIL,
				"Algo inesperado ocorreu no servidor.\nVerifique a corretude dos dados e tente mais tarde."
			);
			$(button).prop("disabled", false)
		}

		$(button).prop("disabled", true)

		BackConfiguracoes.update(function_sucess, function_error);
	}
}

/* --------------------- [Class] BackConfiguracoes --------------------- */
class BackConfiguracoes {
	static update(front_function_sucess, front_function_error) {
		// Dados gerais
		var noIotTempoAtividade = $("#no_iot_tempo_atividade").val()+"";
		var noIotVelocidade = $("#no_iot_velocidade").val()+""
		var bateriaCapacidade = $("#bateria_capacidade").val()+"";
		var consumoAtivado = $("#consumo_ativado").val()+"";
		var consumoDesativado = $("#consumo_desativado").val()+"";

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

		var dado = "";
		dado += "noIotTempoAtividade="+noIotTempoAtividade;
		dado += "&noIotVelocidade="+noIotVelocidade;
		dado += "&bateriaCapacidade="+bateriaCapacidade;
		dado += "&consumoAtivado="+consumoAtivado;
		dado += "&consumoDesativado="+consumoDesativado;

		Ajax("action/configuracoes/configuracoes.php", dado, function_sucess, function_error);
	}
}


/* --------------------- [FunctionPage] Configuracoes --------------------- */
function page_configuracoes() {
	var parametrosUrl = window.location.search.replace("?", "");
	var parametroPage = parametrosUrl.split("=");

	$($("footer a")[0]).attr("data-href", parametroPage[1]+".php");
	$($("footer a")[1]).attr("href", parametroPage[1]+".php");

	$("footer a.salvar").click(function() {
		FrontConfiguracoes.salvar($(this));
	});
}


































/* --------------------- [Class] Controle --------------------- */

class BackControle {
	static iot_ativar() {
		function function_sucess(data) {
			console.log("sucesso");
			console.log(data);
		}
		function function_error(data) {
			console.log("erro");
			console.log(data);
		}

		Ajax("action/controle/iot.php", "", function_sucess, function_error);
	}


	static som_tocar() {
		function function_sucess(data) {
			console.log("sucesso");
			console.log(data);
		}
		function function_error(data) {
			console.log("erro");
			console.log(data);
		}

		var dado = "";
		dado += "operacao=tocar";
		dado += "&valor="+$("#som_volume").val();
		console.log(dado);
		Ajax("action/controle/som.php", dado, function_sucess, function_error);
	}
	static som_parar() {
		function function_sucess(data) {
			console.log("sucesso");
			console.log(data);
		}
		function function_error(data) {
			console.log("erro");
			console.log(data);
		}

		Ajax("action/controle/som.php", "operacao=parar", function_sucess, function_error);
	}
	static som_alterar_volume(button) {
		function function_sucess(data) {
			console.log("sucesso");
			console.log(data);
		}
		function function_error(data) {
			console.log("erro");
			console.log(data);
		}

		var dado = "";
		dado += "operacao=alterar_volume";
		dado += "&valor="+$(button).val();

		Ajax("action/controle/som.php", dado, function_sucess, function_error);
	}
}

/* --------------------- [FunctionPage] Controle --------------------- */
function page_controle() {
	$("button#iot_ativar").click(function() {
		console.log("iot_parar");
		BackControle.iot_ativar();
	});


	$("button#som_tocar").click(function() {
		console.log("som_tocar");
		BackControle.som_tocar();
	});
	$("button#som_parar").click(function() {
		console.log("som_parar");
		BackControle.som_parar();
	});
	$("input#som_volume").change(function() {
		console.log("volume");
		BackControle.som_alterar_volume($(this));
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
