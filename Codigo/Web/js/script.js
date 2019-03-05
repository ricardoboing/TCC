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
		case "listar_evento":
			page_listar_evento();
			console.log("LISTAR_EVENTO")
			break;
		default:
			break;
	}
});

/* --------------------- [Class] IndexCarrinho --------------------- */
var DIRECAO = {
	ANDAR_ESQUERDA: 1,
	PARADO: 0,
	ANDAR_DIREITA: 2
};
var IndexCarrinho = function() {
	this.direcao = DIRECAO.PARADO;
	this.velocidade = 0;
};
IndexCarrinho.prototype.andar_esquerda = function() {
	console.log("ANDAR_ESQUERDA");
};
IndexCarrinho.prototype.andar_direita = function() {
	console.log("ANDAR_DIREITA");
};
IndexCarrinho.prototype.parar = function() {
	console.log("PARAR");
};
IndexCarrinho.prototype.set_velocidade = function(value) {
	console.log("SET_VELOCIDADE");
};

/* --------------------- [Class] IndexSom --------------------- */
var IndexSom = function() {
	this.parado = true;
	this.arquivo = "oie";
};
IndexSom.prototype.parar = function() {
	console.log("parar som");
};
IndexSom.prototype.tocar = function() {
	console.log("tocar som");
};
IndexSom.prototype.set_volume = function(value) {
	console.log("set_volume: "+value);
};
IndexSom.prototype.set_arquivo = function(value) {
	console.log("set_arquivo: "+value);	
};

/* --------------------- [PageFunction] Index --------------------- */
function page_index() {
	var carrinho = new IndexCarrinho();
	var som = new IndexSom();
	
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
var EventoSom = function() {
	this.parado = true;
	this.arquivo = "oie";
};
EventoSom.prototype.ativar = function() {
	$("#som_input_tempo").prop("disabled", false);
	$("#som_input_volume").prop("disabled", false);
	$("#som_input_arquivo").prop("disabled", false);

	$("#som_input_tempo").prop("required", true);
	$("#som_input_volume").prop("required", true);
	$("#som_input_arquivo").prop("required", true);
	console.log("ativar");
};
EventoSom.prototype.desativar = function() {
	$("#som_input_tempo").prop("disabled", true);
	$("#som_input_volume").prop("disabled", true);
	$("#som_input_arquivo").prop("disabled", true);

	$("#som_input_tempo").prop("required", false);
	$("#som_input_volume").prop("required", false);
	$("#som_input_arquivo").prop("required", false);
	console.log("desativar");
};

/* --------------------- [PageFunction] Evento --------------------- */
function page_evento() {
	var som = new EventoSom();

	$("#som_input_checkbox").change(function() {
		var checked = $(this).prop("checked");
		console.log(checked);

		if (checked) {
			som.ativar();
		} else {
			som.desativar();
		}
	});
}

/* --------------------- [Class] EventoSom --------------------- */


/* --------------------- [PageFunction] ListarEvento --------------------- */
function page_listar_evento() {
	$("table input:checkbox").click(function() {
		console.log("ahudhasd");
	});
	$("input:button").click(function() {
		$(window.document.location).attr("href", "evento.html");
	});

}
