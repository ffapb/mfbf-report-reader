<?php

$expected = \yaml_parse_file("expected.yml");
$actual = \yaml_parse_file("actual.yml");

$any = false;
foreach($expected as $account=>$margin) {
  foreach($margin as $type=>$value) {
    $result = $value!=$actual[$account][$type];
    if($result) {
      echo "$account $type margin is wrong".PHP_EOL;
      $any = true;
    }
  }
}

if(!$any) {
  echo "No mistakes".PHP_EOL;
}
