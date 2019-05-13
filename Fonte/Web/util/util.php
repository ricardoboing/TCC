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
function codificar_id($idEmDecimal) {
    // 5 bytes, porem apenas 7 bits sao utilizados em asc2: 2^35 valores
    $idEmDecimal = min($idEmDecimal, 33554432);

    $idEmBits = base_convert($idEmDecimal, 10, 2);
    $idEmBits = formatar_digitos($idEmBits, 25, 0);

    $byte1EmBits = substr($idEmBits, 0, 5);
    $byte2EmBits = substr($idEmBits, 5, 5);
    $byte3EmBits = substr($idEmBits, 10, 5);
    $byte4EmBits = substr($idEmBits, 15, 5);
    $byte5EmBits = substr($idEmBits, 20, 5);

    $byte1 = codificar_asc2($byte1EmBits);
    $byte2 = codificar_asc2($byte2EmBits);
    $byte3 = codificar_asc2($byte3EmBits);
    $byte4 = codificar_asc2($byte4EmBits);
    $byte5 = codificar_asc2($byte5EmBits);

    return $byte1.$byte2.$byte3.$byte4.$byte5;
}
function codificar_horario($hora,$minuto) {
    $minuto += $hora*60;

    $bits = base_convert($minuto, 10, 2);
    $bytesEmBits = formatar_digitos($bits, 15, 0);

    $byte1EmBits = substr($bytesEmBits, 0,5);
    $byte2EmBits = substr($bytesEmBits, 5,5);
    $byte3EmBits = substr($bytesEmBits, 10,5);

    $byte1 = codificar_asc2($byte1EmBits);
    $byte2 = codificar_asc2($byte2EmBits);
    $byte3 = codificar_asc2($byte3EmBits);

    return $byte1.$byte2.$byte3;
}
function codificar_dias_da_semana($domingo,$segunda,$terca,$quarta,$quinta,$sexta,$sabado) {
    $byte1EmBits = $domingo;
    $byte1EmBits .= $segunda;
    $byte1EmBits .= $terca;
    $byte1EmBits .= $quarta;
    $byte1EmBits .= $quinta;
    
    $byte2EmBits = "000";
    $byte2EmBits .= $sexta;
    $byte2EmBits .= $sabado;

    $byte1 = codificar_asc2($byte1EmBits);
    $byte2 = codificar_asc2($byte2EmBits);

    return $byte1.$byte2;
}
function codificar_som($volume,$duracaoEmSegundos) {
    $volumeEmBits = base_convert($volume, 10, 2);
    $volumeEmBits = formatar_digitos($volumeEmBits, 7, "0");

    $duracaoEmBits = base_convert($duracaoEmSegundos, 10, 2);
    $duracaoEmBits = formatar_digitos($duracaoEmBits, 6, "0");

    $byte1EmBits = substr($volumeEmBits, 0,5);
    $byte2EmBits = "000".substr($volumeEmBits, 5,2);
    $byte3EmBits = substr($duracaoEmBits, 0,5);
    $byte4EmBits = "0000".substr($duracaoEmBits, 5,1);

    $byte1 = codificar_asc2($byte1EmBits);
    $byte2 = codificar_asc2($byte2EmBits);
    $byte3 = codificar_asc2($byte3EmBits);
    $byte4 = codificar_asc2($byte4EmBits);

    return $byte1.$byte2.$byte3.$byte4;
}
function codificar_length_nome($lengthEmDecimal) {
    $lengthEmDecimal = min($lengthEmDecimal, 30);
    $lengthEmBinario = base_convert($lengthEmDecimal, 10, 2);
    $lengthEmBinario = formatar_digitos($lengthEmBinario, 5, 0);

    $byte1 = codificar_asc2($lengthEmBinario);

    return $byte1;
}
function codificar_inteiro($inteiro) {
    $inteiroEmDecimal = min($inteiro, 255);
    $inteiroEmBinario = base_convert($inteiroEmDecimal, 10, 2);
    $inteiroEmBinario = formatar_digitos($inteiroEmBinario, 5, 0);

    $byte1 = codificar_asc2($inteiroEmBinario);

    return $byte1;
}
function codificar_asc2($valorBinario) {
    $valorDecimal = base_convert("10".$valorBinario, 2, 10);
    return chr($valorDecimal)."";
}
?>