<?php
// include("db_conn.php");
// data_default_timezone_set('Asia/Taipei');
header("Content-Type:text/html; charest=utf-8");
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
$Account = $_POST['Account'];
$userPw = sha1($_POST["password"]);
$sql = "SELECT * FROM `user_data` WHERE `account` = '$Account' AND `password` = sha1('$passPW')";
$result = mysqli_query($link, $sql);
$val = $result->num_rows;
if($val == 1){
    $outData = array("status" => "success");
    echo 'Login success!';
}else{
    $outData = array("status" => "noAccount");
    echo "noAccount";
}
// if(isset($_POST)){
// }else{
//     $outData = array("status" => "fail");
// }
// echo json_encode($outData, JSON_UNESCAPED_UNICODE);