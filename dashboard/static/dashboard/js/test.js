var xField = 'Date';
var yField = 'Mean_TemperatureC';

var selectorOptions = {
    buttons: [],
};

Plotly.d3.csv(rawDataURL, function(err, rawData) {
    if(err) throw err;

    var data = prepData(rawData);
    var layout = {
        title: 'Time series with range slider and selectors',
        xaxis: {
            rangeselector: selectorOptions,
            rangeslider: {}
        },
        yaxis: {
            fixedrange: true
        }
    };

    Plotly.newPlot('myDiv', data, layout);
});

function prepData(rawData) {
    var x = [];
    var y = [];

    rawData.forEach(function(datum, i) {

        x.push(new Date(datum[xField]));
        y.push(datum[yField]);
    });

    return [{
        mode: 'lines',
        x: x,
        y: y
    }];
}