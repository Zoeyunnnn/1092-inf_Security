<?php
include('db_conn.php');
$id = $_GET['seID'];
$sql1 = "SELECT id FROM `seLog` WHERE `uniqueID` = '$id' and `clickLink_time` IS NULL; ";
$result = mysqli_query($link, $sql1);
if (mysqli_num_rows($result) == 1) {
    $row = mysqli_fetch_assoc($result);
    $sql2 = "UPDATE `seLog` SET `clickLink_time` = CURRENT_TIMESTAMP WHERE `id` = " . $row['id'] . ";";
    mysqli_query($link, $sql2);
}
