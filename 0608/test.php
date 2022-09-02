<?php
header("X-XSS-Protection: 0;");
$name = $_POST['name'];
echo $name;