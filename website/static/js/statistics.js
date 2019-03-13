    var xScale, yScale, xAxis, yAxis, svg, yAxisUpdate;
    var histogram = d3.layout.histogram()
                    .range([0, 100])
                    .bins(10)
                    .frequency(false);
    // dimensions
    var padding = {left:50, right:50, top:50, bottom:50},
            width = 500 - padding.left - padding.right,
            height = 500 - padding.top - padding.bottom;

    var page = d3.select('#page-statistics');

    // load data from csv
    d3.csv(dataset_url,function(csvdata){
            var dataset = csvdata.map(function(d) {
                return {
                    age: +d.Age,
                    sex: d.Sex
                }
            });
            var initialData = dataset.map(function(d) { return d.age; });
            hist(initialData);

            var dropdownChange = function(){
                var selection = d3.select("#gender").node().value;
                var newData = dataset.map(function(d) { return d.age; });
                if (selection != "Both") {
                    newData = dataset.filter(function(d) { return d.sex == selection; });
                    newData = newData.map(function(d) { return d.age; });
                };
                update(newData);
            };
            // monitor change in dropdown
            var dropdown = d3.select("#gender")
                           .on("change", dropdownChange);
        });

    // make histogram
    var hist = function(dataset){
        var data = histogram(dataset);

        xScale = d3.scale.ordinal()
            .domain(d3.range(0, 101, 10))
            .rangeRoundBands([0, width]);

        yScale = d3.scale.linear()
            .domain([0, d3.max(data, function(d) { return d.length; })])
            .range([height, 0]);

        xAxis = d3.svg.axis()
            .scale(xScale)
            .orient("bottom");

        yAxis = d3.svg.axis()
            .scale(yScale)
            .orient("left");

        // create canvas
        svg = d3.select(".vis")
            .append("svg")
            .attr("width", width + padding.left + padding.right)
            .attr("height", height + padding.top + padding.bottom)
            .append("g")
            .attr("transform", "translate(" + padding.left + "," + padding.top + ")");

        // enter new
        var bar = svg.selectAll(".bar")
            .data(data)
            .enter()
            .append("g")
            .attr("class", "bar")
            .attr("transform", function(d) { return "translate(" + xScale(d.x) + "," + yScale(d.length) + ")"; });

        bar.append("rect")
            .attr("x", xScale(data[0].dx)/2 + 1)
            .attr("width", xScale(data[0].dx) - xScale(0) - 1)
            .attr("height", function(d) { return height - yScale(d.length); })
            .attr("fill","#645394")
            .on("mouseover", function(d,i){
                d3.select(this)
                    .attr("fill","DarkOrange");
                tooltip.style("display", "block");
            })
            .on("mouseout", function(d,i){
                d3.select(this)
                    .transition()
                    .duration(100)
                    .attr("fill","#645394");
                tooltip.style("display", "none");
            })
            .on("mousemove", function(d,i) {
                var xPosition = d3.event.pageX;
                var yPosition = d3.event.pageY;

                var corr = {x: page[0][0].offsetLeft + padding.left, y: page[0][0].offsetTop + padding.top};

                tooltip.attr("transform", "translate(" + (xPosition-corr.x) + "," + (yPosition-corr.y) + ")");
                tooltip.select("text").text(d3.format(".2%")(d.y));
            });

        bar.append("text")
            .attr("dy", ".75em")
            .attr("y", -15)
            .attr("x", (xScale(data[0].dx)-xScale(0))/2 + xScale(data[0].dx)/2)
            .attr("text-anchor", "middle")
            .text(function(d) { return d.length; });

        svg.append("g")
            .attr("class","axis")
            .attr("transform","translate(" + 0 + "," + height + ")")
            .call(xAxis)
            .append("text")
            .attr("class", "label")
            .attr("x", width+padding.right)
            .attr("y", 15)
            .attr("font-size", "30px")
            .style("text-anchor", "end")
            .text("Age");

        yAxisUpdate = svg.append("g")
            .attr("class","axis")
            .attr("transform","translate(" + 0 + "," + 0 + ")")
            .call(yAxis);

        yAxisUpdate.append("text")
            .attr("class", "label")
            .attr("transform", "rotate(-90)")
            .attr("y", 0)
            .attr("dy", ".9em")
            .attr("font-size", "15px")
            .style("text-anchor", "end")
            .text("Number of patients");

        var tooltip = svg.append("g")
          .attr("class", "tooltip1")
          .style("display", "none");

        tooltip.append("rect")
          .attr("width", 50)
          .attr("height", 20)

        tooltip.append("text")
          .attr("x", 25)
          .attr("y", 15)
    };

    // update histogram
    var update = function(newData){
        var data = histogram(newData);

        // reset y axis
        yScale.domain([0, d3.max(data, function(d) { return d.length; })]);
        yAxisUpdate.transition()
            .call(yAxis);

        var bar = svg.selectAll(".bar")
            .data(data);

        // remove
        bar.exit().remove();

        // update
        bar.transition()
            .duration(200)
            .attr("transform", function(d) { return "translate(" + xScale(d.x) + "," + yScale(d.length) + ")"; });

        bar.select("rect")
            .transition()
            .duration(200)
            .attr("height", function(d) { return height - yScale(d.length); });

        bar.select("text")
            .transition()
            .duration(200)
            .text(function(d) { return d.length; });
        };