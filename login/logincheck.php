<?php
include("db_conn.php");
// data_default_timezone_set('Asia/Taipei');
header("Content-Type:text/html; charest=utf-8");
header("Access-Control-Allow-Origin: *");

$link -> set_charset("utf8");
$Account = $_POST['Account'];
$userPw = $_POST["password"];
$sql = "SELECT * FROM `user_data` WHERE `account` = '$Account' AND `password` = '$userPw'";
echo $sql;
$result = mysqli_query($link, $sql);
$val = $result->num_rows;
if($val == 1){
    $outData = array("status" => "success");
    echo 'Login success!';
}else{
    $outData = array("status" => "noAccount");
    echo "Login Error";
}
// if(isset($_POST)){
// }else{
//     $outData = array("status" => "fail");
// }
// echo json_encode($outData, JSON_UNESCAPED_UNICODE);