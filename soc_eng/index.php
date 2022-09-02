<?php
	$mailUniqueID = uniqid();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>ZOE</title>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <script src="https://kit.fontawesome.com/e5f052c807.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

    <script src="js/jquery-3.5.1.js" type="text/javascript"></script>
    <link rel="stylesheet" type="text/css" href="index.css">
</head>
<body>
    <div id="login">
        <!-- <h3 class="text-center text-white pt-5">Login</h3> -->
        <div class="container">
            <div id="login-row" class="row justify-content-center align-items-center">
                <div id="login-column" class="col-md-6">
                    <div id="login-box" class="col-md-12">
                        <form id="login-form" class="form" action="sendMail.php" method="post">
                            <h3 class="text-center text-info">sendMail</h3>
                            <div class="form-group">
                                <label for="uniqueID" class="text-info">Unique ID:</label><br>
                                <input type="text" name="uniqueID" id="uniqueID" class="form-control" readonly value="<?php echo $mailUniqueID; ?>">
                            </div>
                            <div class="form-group">
                                <label for="receiverName" class="text-info">Name:</label><br>
                                <input type="text" name="receiverName" id="receiverName" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="receiverEmail" class="text-info">E-mail:</label><br>
                                <input type="text" name="receiverEmail" id="receiverEmail" class="form-control">
                            </div>
                            <div class="form-group">
                                <!-- <label for="remember-me" class="text-info"><span>Remember me</span> <span><input id="remember-me" name="remember-me" type="checkbox"></span></label><br> -->
                                <input type="submit" name="submit" class="btn btn-info btn-md" value="submit">
                            </div>
                            <!-- <div id="register-link" class="text-right">
                                <a href="#" class="text-info">Register here</a>
                            </div>
                            <br/> -->
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
