<?php
header("Access-Control-Allow-Origin: *");
$link = mysqli_connect(
    "localhost",
    "sqlinjUser",
    "Sq95j7#o",
    "sqlinjUser"
);

if(!$link){
    echo "Error! Unable to connect to MySQL." . PHP_EOL;
    echo "Debugging errno:" . mysqli_connect_errno() . PHP_EOL;
    echo "Debugging errno:" . mysqli_connect_error() . PHP_EOL;
}

$link -> set_charset("utf8");