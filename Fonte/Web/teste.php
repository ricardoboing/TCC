<?php
include "util/util.php";

echo "\"".codificar_som("1", "100", "60")."\"";
echo "<br>";
echo "\"".codificar_dias_da_semana(1,1,1,1,0,0,1)."\"";
echo "<br>";
echo "\"".codificar_hora("24", "59")."\"";
echo "<br>";
echo "\"".codificar_id("4294967296")."\"";
echo "<br>";
echo base_convert(4294967295, 10, 2);
/*
$a = "011111";


echo $a;
echo "<br>";
$b = base_convert($a, 2, 10);

echo $b;
echo "<br>";
echo chr($b);*/
?>