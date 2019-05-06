// from data.js

function showTable (dataset){

    var data = dataset;
    //}
    var tbody = d3.select("tbody");
    
    
    // YOUR CODE HERE!
    
    data.forEach((ufoReport) => {
        var row = tbody.append("tr");
        Object.entries(ufoReport).forEach(([key, value]) => {
          var cell = tbody.append("td");
          cell.text(value);
        });
      });
    };
    
    showTable(data);
    
    // YOUR CODE HERE!
    
    