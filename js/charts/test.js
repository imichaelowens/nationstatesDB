$(document).read(function(){
  var options = {
    chart: {
      renderTo: 'container',
      type: 'line'
    },
    series: [{}]
  };
  $.getJSON('data.php'), function(data){
    options.series[0].data = data;
    var chart = new Highcharts.Charts(options);
  }
});