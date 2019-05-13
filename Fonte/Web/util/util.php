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
/*
echo "4: ".formatar_digitos("1234567", 4, "0")."<br>";
echo "4: ".formatar_digitos("12", 4, "9")."<br>";
echo "4: ".formatar_digitos("1", 4, "0")."<br>";
echo "6: ".formatar_digitos("123", 6, "0")."<br>";
echo "6: ".formatar_digitos("1234", 6, "9")."<br>";
*/
?>