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

/* --------------------- [Class] IndexTarifa --------------------- */
var IndexTarifa = function() {
	
};
IndexTarifa.prototype.adicionarTarifa = function(button) {
	var trMenu = $(button).parents("tr.menu")[0];
	var table = $(button).parents("table")[0];
	
	var trClonada = $(table).find("tr")[1];
	var trClone = $(trClonada).clone();

	$(trMenu).remove();
	$(trClonada).parent().append(trClone);
	$(trClonada).parent().append(trMenu);

	$(trClone).find("button.remover").click(function() {
		indexTarifa.removerTarifa($(this));
	});

	$(trMenu).find("button.adicionar").click(function() {
		indexTarifa.adicionarTarifa($(this));
	});

	$(trMenu).find("button.salvar").click(function() {
		indexTarifa.salvarTarifa();
	});

	$(table).find("button.remover").prop("disabled", false);
};
IndexTarifa.prototype.salvarTarifa = function() {
	
};
IndexTarifa.prototype.removerTarifa = function(button) {
	var trPai = $(button).parents("tr")[0];
	var elementoAvo = $(trPai).parent();

	var numeroFilhosDoAvo = $(elementoAvo).find("tr").length;

	// Se o "avo" do elemento possuir duas ou menos tr
	if (numeroFilhosDoAvo <= 3) {
		return;
	}

	$(trPai).remove();

	if (numeroFilhosDoAvo <= 4) {
		var ultimaTrDeTarifa = $(elementoAvo).find("tr")[1];
		$(ultimaTrDeTarifa).find("button.remover").prop("disabled", true);
	}
};


/* --------------------- [PageFunction] Index --------------------- */
function page_index() {
	this.indexTarifa;
	indexTarifa = new IndexTarifa();

	$("table.tarifa button.remover").click(function() {
		indexTarifa.removerTarifa($(this));
	});

	$("table.tarifa button.adicionar").click(function() {
		indexTarifa.adicionarTarifa($(this));
	});

	$("table.tarifa button.salvar").click(function() {
		indexTarifa.salvarTarifa();
	});
}

/* --------------------- [Class] ManualCarrinho --------------------- */
var DIRECAO = {
	ANDAR_ESQUERDA: 1,
	PARADO: 0,
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

/* --------------------- [PageFunction] Index --------------------- */
function page_manual() {
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

/* --------------------- [Class]  --------------------- */


/* --------------------- [PageFunction] Horarios --------------------- */
function page_horarios() {
	$("table input:checkbox").click(function() {
		console.log("active checkbox");

		var tr;
		tr = $(this).parents("tr")[0];
		
		var disabled;
		disabled = $(tr).hasClass("disabled");

		if (disabled) {
			$(tr).removeClass("disabled");
		} else {
			$(tr).addClass("disabled");
		}
	});
	$("input:button").click(function() {
		$(window.document.location).attr("href", "evento.html");
	});
}
