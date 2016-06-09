var http = require('http');
var express = require('express');
var getenv = require('getenv');

var app = express();

var port = getenv('PORT');

var random = function(low, high) {
    return Math.random() * (high - low) + low;
}


var randint = random(0, 1000);
app.get('/*', function (req, res) {
    res.json({'yourint': randint});
})

app.listen(port, function(){
    console.log(`Listening on ${port}`)
})
