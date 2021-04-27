<?php

    $server   = "localhost";
    $database = "nationcensusdata";
    $username = "root";
    $password = "";

    try{
        $dbcon = new PDO("mysql:host={$server};dbname={$database}",$username,$password);
        $dbcon->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    }catch(PDOException $ex){

        die($ex->getMessage());
    }

    $stmt=$dbcon->prepare("SELECT waCategory, count(*) as c FROM census0 GROUP BY waCategory");
    $stmt->execute();
    while($row=$stmt->fetch(PDO::FETCH_ASSOC)){
        extract($row);
        /*echo($waCategory);
        echo($c);*/
        $json[]= [$waCategory, $c];
    }
    echo json_encode($json);
?>