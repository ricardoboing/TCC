<?php

function formatar_digitos($valor, $numeroDeDigitosEsperado, $digitoDePreenchimento) {
    $numeroDeDigitosEsperado = intval($numeroDeDigitosEsperado);
    $valorStr = $valor."";
    $lenghtValor = strlen($valorStr);
    $digitoDePreenchimento = "".$digitoDePreenchimento;

    if ($lenghtValor > $numeroDeDigitosEsperado) {
        $valorStr = substr($valorStr, 0, $numeroDeDigitosEsperado);
        return $valorStr;
    }
    
    $numeroDeDigitosEmFalta = $numeroDeDigitosEsperado - $lenghtValor;

    for ($c = 0; $c < $numeroDeDigitosEmFalta; $c++) {
        $valorStr = $digitoDePreenchimento.$valorStr;
    }
	
    return $valorStr;
}
?>