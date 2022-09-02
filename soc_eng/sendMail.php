<?php
include("db_conn.php");
date_default_timezone_set('Asia/Taipei');
$uniqueID = $_POST['uniqueID'];
$receiverName = $_POST['receiverName'];
$receiverEmail = $_POST['receiverEmail'];
$sql = "INSERT INTO `seLog`(`name`, `uniqueID`, `Email`)
VALUES ('" . $receiverName . "','" . $uniqueID . "','" . $receiverEmail . "');";

if (mysqli_query($link, $sql)) {
    echo "<h2 style='text-align:center;color: blue;'>Saving to seLog table success!</h2>";
    echo "<h2 style='text-align:center;color: gray;'>請將此段連結放到你社交⼯程信件裡<br/> &lt;img src='http://120.108.111.150:18080/~zoe/openMailLog.php?seID=" . $uniqueID . "' width=0 height=0 &gt;</h2>";
    echo "<h2 style='text-align:center;color: gray;'>請將此段連結放到你社交⼯程信件裡要讓使⽤者點擊的連結處<br/> &lt;a href='http://120.108.111.150:18080/~zoe/clickLinkLog.php?seID=" . $uniqueID . "' &gt;要讓使用者點的文字&lt;/a&gt;</h2>";
    echo "<a class='btn' href='index.php' style='text-align: center; width: 120px;height:30px; font-size:1.2em; margin: 0 auto 0 auto;'>返回首頁</a>";
    // echo '<meta http-equiv="refresh" content="5;URL=index.php" />';
} else {
    echo "can't save record to data table";
}