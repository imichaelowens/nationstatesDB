Highcharts.chart('container', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Most Successful Government Types, 2021'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Government Classifications',
        colorByPoint: true,
        data: [{
            name: 'Iron Fist Consumerists',
            y: 4322,
            sliced: true,
            selected: true
        }, {
            name: 'Innofensive Centrist Deomcracy',
            y: 4301
        }, {
            name: 'Anarchy',
            y: 3826
        }, {
            name: 'Democratic Socialists',
            y: 3736
        }, {
            name: 'Psychotic Dictatorships',
            y: 3322
        }, {
            name: 'Left Wing Utopia',
            y: 3252
        }, {
            name: 'Civil Rights Lovefest',
            y: 3021
        }, {
            name: 'Father Knows Best State',
            y: 2352
        }, {
            name: 'Corporate Police State',
            y: 2048
        }, {
            name: 'Left-Leaning College State',
            y: 1517
        }, {
            name: 'Capitalist Paradise',
            y: 1490
        }, {
            name: 'Compulsory Consumerist State',
            y: 1345
        }, {
            name: 'Liberal Democratic Socialists',
            y: 1344
        }, {
            name: 'New York Times Democracy',
            y: 1270
        }, {
            name: 'Corrupt Dictatorship',
            y: 1185
        }, {
            name: 'Scandinavian Liberal Paradise',
            y: 1083
        }, {
            name: 'Capitalizt',
            y: 2048
        }, {
            name: 'Moralistic Democracy',
            y: 548
        }, {
            name: 'Corporate Bordello',
            y: 458
        }, {
            name: 'Authoritarian Democracy',
            y: 376
        }, {
            name: 'Benevolent Dictatorship',
            y: 227
        }, {
            name: 'Libertarian Police State',
            y: 217
        }, {
            name: 'Mother Knows Best State',
            y: 200
        }, {
            name: 'Right-wing Utopia',
            y: 108
        }, {
            name: 'Iron Fist Socialists',
            y: 88
        }, {
            name: 'Tyranny by Majority',
            y: 68
        }, {
            name: 'Conservative Democracy',
            y: 39
        }, {
            name: 'Free Market Paradise',
            y: 39
        }]
    }]
});