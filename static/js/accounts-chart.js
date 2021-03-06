/* acounts data */
var margin = {top: 20, right: 20, bottom: 30, left: 40},
width = 600 - margin.left - margin.right,
height = 400 - margin.top - margin.bottom;

var formatPercent = d3.format(".0%");

var x = d3.scale.ordinal()
.rangeRoundBands([0, width], .1)
.domain(data.map(function(d) { return d["date"];}));

var y = d3.scale.linear()
.range([height, 0])
.domain([0, d3.max(data, function(d) { return d["yuan"]; })]);

var xAxis = d3.svg.axis()
.scale(x)
.orient("bottom");

var yAxis = d3.svg.axis()
.scale(y)
.orient("left");

var svg = d3.select(".chart").select("#chart").append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

svg.append("g")
.attr("class", "x axis")
.attr("transform", "translate(0," + height + ")")
.call(xAxis);

svg.append("g")
.attr("class", "y axis")
.call(yAxis)
.append("text")
.attr("transform", "rotate(-90)")
.attr("y", 6)
.attr("dy", ".71em")
.style("text-anchor", "end")
.text("Yuan");

svg.selectAll(".bar")
.data(data)
.enter().append("rect")
.attr("class", "bar")
.attr("x", function(d) { return x(d["date"]); })
.attr("width", x.rangeBand())
.attr("y", function(d) { return y(d["yuan"]); })
.attr("height", function(d) { return height - y(d["yuan"]); });
