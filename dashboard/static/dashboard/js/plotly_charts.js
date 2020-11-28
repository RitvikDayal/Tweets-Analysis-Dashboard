$.ajax({
    method: "GET",
    url: '/api/data/summary/?format=json',

    // ON SUCCESS
    success: function(summary){
        console.log(summary);

        // Horizontal Bar Plot on Covid Stats
        var trace = {
            x: summary.covid_stats.values,
            y: summary.covid_stats.labels,
            name: 'Covid Statistics',
            orientation: 'h',
            type: 'bar',
            marker: {
              color: 'rgba(255,153,51,0.6)',
              width: 1
            }
          };
          
          var data = [trace];
          
          var layout = {
            title: 'Covid Statistics',
            barmode: 'stack'
          };
          
          Plotly.newPlot('barhChart', data, layout);

    },

    //ON FALIURE
    error: function(error_data){
        console.log('Error Occured!!')
        console.log(error_data)
    }
})

$.ajax({
    method: "GET",
    url: '/api/data/summary/?format=json',
 
    // ON SUCCESS
    success: function(summary){
        // Pie Chart
        var ctx = document.getElementById('pieChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: summary.Y,
                datasets: [{
                    label: 'Number of People',
                    data: summary.X,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    xAxes: [{
                        gridLines: {
                            display: false,                            
                            color: "rgba(0, 0, 0, 0)",
                        },
                        ticks: {
                            display: false
                        }
                    }],
                    yAxes: [{
                        gridLines: {
                            display: false,
                            color: "rgba(0, 0, 0, 0)",
                        },
                        ticks: {
                            display: false
                        }
                    }]
                }
            }
        });
    },

    //ON FALIURE
    error: function(error_data){
        console.log('Error Occured!!')
        console.log(error_data)
    }
})

$.ajax({
    method: "GET",
    url: '/api/data/dateWiseTweets/?format=json',

    // ON SUCCESS
    success: function(data){
        console.log(data);

        // Horizontal Bar Plot on Covid Stats
        
        var tweets = {
            x: data.X,
            y: data.Y,
            type: 'scatter'
        };

        var selectorOptions = {
            buttons: [],
        };

        var layout = {
            title: 'Time series Tweets',
            xaxis: {
                rangeselector: selectorOptions,
                rangeslider: {}
            },
            yaxis: {
                fixedrange: true
            }
        };
          
        var data = [tweets];
          
        Plotly.newPlot('lineChart', data, layout);

    },

    //ON FALIURE
    error: function(error_data){
        console.log('Error Occured!!')
        console.log(error_data)
    }
})

$.ajax({
    method: "GET",
    url: '/api/data/wordCount/?format=json',

    // ON SUCCESS
    success: function(data){
        console.log(data);

        // Horizontal Bar Plot on Word Count
        // All Words
        var trace1 = {
            x: data.allwords.freq,
            y: data.allwords.words,
            name: 'Word Count',
            orientation: 'h',
            type: 'bar',
            marker: {
              color: 'rgba(255,153,51,0.6)',
              width: 1
            }
          };
          
          var data1 = [trace1];
          
          var layout = {
            title: 'Word Count',
            barmode: 'stack'
          };
          
          Plotly.newPlot('allwords', data1, layout);

          // Neutral Words
          var trace2 = {
            x: data.neuwords.freq,
            y: data.neuwords.words,
            name: 'Word Count',
            orientation: 'h',
            type: 'bar',
            marker: {
              color: 'rgba(31, 119, 180, 0.6)',
              width: 1
            }
          };
          
          var data2 = [trace2];
          
          Plotly.newPlot('neuwords', data2, layout);

          // Positive Words
          var trace3 = {
            x: data.poswords.freq,
            y: data.poswords.words,
            name: 'Word Count',
            orientation: 'h',
            type: 'bar',
            marker: {
              color: 'rgba(44, 160, 44, 0.6)',
              width: 1
            }
          };
          
          var data3 = [trace3];
          
          Plotly.newPlot('poswords', data3, layout);

          // Negative Words
          var trace4 = {
            x: data.negwords.freq,
            y: data.negwords.words,
            name: 'Word Count',
            orientation: 'h',
            type: 'bar',
            marker: {
              color: 'rgba(214, 39, 40, 0.6)',
              width: 1
            }
          };
          
          var data4 = [trace4];
          
          Plotly.newPlot('negwords', data4, layout);

    },

    //ON FALIURE
    error: function(error_data){
        console.log('Error Occured!!')
        console.log(error_data)
    }
})

var tweets = jQuery(".tweet");

jQuery(tweets).each(function(t, tweet) {
    var id = jQuery(this).attr('id');
    twttr.widgets.createTweet(
        id, tweet, {
        conversation: 'none', // or all
        cards: 'hidden', // or visible 
        linkColor: '#cc0000', // default is blue
        theme: 'light' // or dark
        });

});
