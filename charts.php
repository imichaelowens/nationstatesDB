<?php
	include 'database.php';
	$queryEconomy = "SELECT nationEconomy, waCategory, count(*) as c FROM theWorld GROUP BY nationEconomy ORDER BY `c` DESC";
  $queryCivilRights = "SELECT civilRights, waCategory, count(*) as c FROM theWorld GROUP BY civilRights ORDER BY `c` DESC";
  $queryPoliticalFreedom = "SELECT politicalFreedom, waCategory, count(*) as c FROM theWorld GROUP BY politicalFreedom ORDER BY `c` DESC";
  $actionPoliticalFreedom = mysqli_query($conn, $queryPoliticalFreedom);
  $actionCivilRights = mysqli_query($conn, $queryCivilRights);
  $actionNationEconomy = mysqli_query($conn, $queryEconomy);
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <!-- required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>NationStates Census Strategies</title>
  <!-- Bootstrap CSS local file -->
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <link rel="stylesheet" href="css/main.css">
</head>

<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <div class="container">
        <a class="navbar-brand" href="#">Nation States Census Database</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
                <a class="nav-link" href="index.html">About Project</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="charts.html">Census Charts
                <span class="sr-only">(current)</span>
                </a>
            </li>
            </ul>
        </div>
        </div>
    </nav>
    <!-- End Navigation Bar -->

    <!-- Header Image Here -->
    <header class="py-5 bg-image-full" style="background-image: url('images/roman_columns.jpg');">
        <img class="img-fluid d-block mx-auto" src="images/nationstates_bl_bg.jpg" alt="NationStates Census Database">
        <!-- Image from UnSplash: https://unsplash.com/photos/o0kbc907i20 -->
    </header>
    <!-- End Header Image -->

<!-- Charts -->
<div class="row p-2">
  <div class="col col-md-6 mx-auto">
    <figure class="highcharts-figure">
        <div id="container"></div>
        <p class="highcharts-description p-2 text-wrap">
            Data presented in this chart is for a total of 42,500 nations. All of these nations belong in the top 500 of one WA census report but none are duplicated or belong to more then one to prevent double counting. A surprising thing is revealed - Anarchy or no government seems to be a successful form of government when playing NationStates. NationStates is not real life, and I attribute the more extreme forms of government being popular due to the game giving the player funny or interesting choices when playing thus leading to Anarchy or another form of not mainstream government.
        </p>
      </figure>
  </div>
</div>
 
<!-- DB UPDATE -->
<div class="row p-2 mx-auto">
  <div class="col text-center">
    <p><i>Database last updated on 4/25/2020 12:05PM</i></p>
  </div>
</div>
<!-- DB UPDATE -->
<!-- Political Freedom -->
<div class="row p-2 mx-auto">
  <div class="col text-center">
    <button class="btn btn-primary mx-auto" type="button" data-toggle="collapse" data-target="#politicalFreedomTable" aria-expanded="false" aria-controls="collapseExample">
        View Most Common Poltical Freedom Coorelations
      </button>
  </div>
</div>

<div class="row p-2 collapse" id="politicalFreedomTable">
        <table class="col col-lg-6 mx-auto table table-dark table-striped"><!-- Begin Table -->
            <tr>
                <th>Politcal Freedom</th>
                <th>WA Category</th>
                <th>Number of Nations</th>
            </tr>
            <?php while ($row = mysqli_fetch_assoc($actionPoliticalFreedom)) :  ?>
                <tr>

                    <td><?php echo $row['politicalFreedom']; ?></td>
                    <td><?php echo $row['waCategory']; ?></td>
                    <td><?php echo $row['c']; ?></td>
                </tr><!-- end of HTML table row -->
            <?php endwhile;  ?>
        </table>
        <div class="row text-center mx-auto">
          <div class="col col-md-4 text-center mx-auto">
            <p class="text-center p1">This query on the database shows the correlation between the Different WA Categories and the amount of Political Freedom citizens in the nation have. By definition - dictatorships generally do not have many political rivals or much poltiical speech. We see real life examples coming through in NationStates here by the contrasting amount of dictatorships and "Civil Rights Lovefest" or similiar nations and their coresponding political freedom values. We learn that by going on a dictatorship route of play citizens will most likely lose thier poltiical freedom.  </p>
            </div>
          </div>
    </div>

<!-- End Political Freedom -->
<!-- Civil Rights -->
<div class="row p-2 mx-auto">
  <div class="col text-center">
    <button class="btn btn-primary mx-auto" type="button" data-toggle="collapse" data-target="#civilRightsTable" aria-expanded="false" aria-controls="collapseExample">
        View Most Common Civil Rights Coorelations
      </button>
  </div>
</div>

<div class="row p-2 collapse" id="civilRightsTable">
        <table class="col col-lg-6 mx-auto table table-dark table-striped"><!-- Begin Table -->
            <tr>
                <th>Civil Rights Status</th>
                <th>WA Category</th>
                <th>Number of Nations</th>
            </tr>
            <?php while ($row = mysqli_fetch_assoc($actionCivilRights)) :  ?>
                <tr>

                    <td><?php echo $row['civilRights']; ?></td>
                    <td><?php echo $row['waCategory']; ?></td>
                    <td><?php echo $row['c']; ?></td>
                </tr><!-- end of HTML table row -->
            <?php endwhile;  ?>
        </table>
        <div class="row text-center mx-auto">
          <div class="col col-md-4 text-center mx-auto">
            <p class="text-center p1">This query on the database shows the correlation between the Different WA Categories and the amount of Civil Rights citizens in the nation have. Understandably, the most populous nation type for the best civil rights is "Civil Rights Lovefest". The second most popular correlation was "Psychotic Dictatorship"
              and outlawed civil rights. I think this is because of the two most fun styles of playing: being an evil dictator or trying to be the best leader possible. This type of thinking seems to also be correlative also to the "Capitalist" nations being somewhat free for civil rights which helps with economic activity.   </p>
            </div>
          </div>
    </div>
<!-- End Civil Rights -->
<!-- Economy -->
<div class="row p-2 mx-auto">
  <div class="col text-center">
    <button class="btn btn-primary mx-auto" type="button" data-toggle="collapse" data-target="#economyTable" aria-expanded="false" aria-controls="collapseExample">
        View Most Common Economic Coorelations
      </button>
  </div>
</div>

<div class="row p-2 collapse" id="economyTable">
        <table class="col col-lg-6 mx-auto table table-dark table-striped"><!-- Begin Table -->
            <tr>
                <th>Economic Rating</th>
                <th>WA Category</th>
                <th>Number of Nations</th>
            </tr>
            <?php while ($row = mysqli_fetch_assoc($actionNationEconomy)) :  ?>
                <tr>

                    <td><?php echo $row['nationEconomy']; ?></td>
                    <td><?php echo $row['waCategory']; ?></td>
                    <td><?php echo $row['c']; ?></td>
                </tr><!-- end of HTML table row -->
            <?php endwhile;  ?>
        </table>
        <div class="row text-center mx-auto">
          <div class="col col-md-4 text-center mx-auto">
            <p class="text-center p1">This query on the database shows the correlation between the Different WA Categories and the economic rating of the nation. Interestingly, many of the "left leaning" nations had worse economic ratings then the dictatorships and "capitalist" nations. This is most likely because of the higher personal taxes the player has to choose in order to have better social services. I was also surprised that many nations classified as "Anarchy" had good economic ratings. Less regulation (because of no government) most likely played a roll in this.   </p>
            </div>
          </div>
    </div>
<!-- End Economy -->
<!-- End Charts -->

<!-- Footer -->
  <footer class="py-5 bg-dark">
    <div class="container">
      <p class="m-0 text-center text-white">Copyright &copy; Michael Owens 2021 | Image by: Katie Moum on <a href="https://unsplash.com/photos/o0kbc907i20">UnSplash</a> </p>
    </div>
  </footer>
<!-- End Footer -->

<!-- Scripts -->
    <script src="js/jquery-3.1.1.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <!-- Begin HighCharts CDN-->
    <script src="https://code.highcharts.com/highcharts.js"></script>
    <!-- Chart Theme -->
    <script src="https://code.highcharts.com/themes/sand-signika.js"></script>
    <!-- Add Grid For Easier Reading -->
    <script src="https://code.highcharts.com/themes/grid.js"></script>
    <!-- Export Controls -->
    <script src="https://code.highcharts.com/modules/exporting.js"></script>
    <!--END HighCharts CDN -->
    

    <!-- My Charts -->
    <script src="js/charts/worldGovernmentStyle.js"></script>
    <!-- End My Charts -->

<!-- End Scripts -->

</body>
</html>