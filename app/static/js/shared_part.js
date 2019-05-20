
function log_out_show(){
  var logout_part = document.getElementById('logout-part');
  logout_part.style.display = "block";
}



function close_window(event){
  event.target.parentNode.parentNode.style.display = 'none';
}


// -------------The Part Cannot Be Removed----------------------
$(document).ready(function() {
    $("#Add").on("click", function() {
        $("#textboxDiv").append("<div><br>New Option :<input class='poll-option form-control' type='text' placeholder='New Option'/></div>");
    });
    $("#Remove").on("click", function() {
        $("#textboxDiv").children().last().remove();
    });

    var time = document.lastModified.split(" ")[0];
    var time_str = '<p class="font-8">Created by <a href="https://www.facebook.com/profile.php?id=100017465704093" class="text-lightgrey" target="_blank">Minrui Lu</a> and <a class="text-lightgrey" href="https://www.facebook.com/sub1433">Wenjing Zheng</a>' +'<span>&nbsp&nbsp&nbsp&nbspLast Modified Date Was: </span>'+ time +'</p>'
    $("footer").append(time_str);

    // Part for doughnut chart
    var total =0;
    for (var i=0;i<values.length;i++){
      total += values[i];
    }

    var pie_values = [];

    for(i =0;i<values.length;i++){
      pie_values.push(Math.round(values[i]/total * 100));
    }
    var canvas = document.getElementById("pieChart");
    ctx2 = canvas.getContext('2d');
    canvas.style.backgroundColor="#fff";

    Chart.defaults.global.defaultFontColor = 'black';
    Chart.defaults.global.defaultFontSize = 16;
    var theHelp = Chart.helpers;

    var data = {
      labels: label,
      datasets: [{
        fill: true,
        backgroundColor: ["rgba(48, 145, 222, 0.82)", "rgba(136, 58, 221, 0.82)","rgba(238, 193, 80, 0.82)","rgba(240, 87, 207, 0.82)","rgba(247, 135, 239, 0.82)","rgba(238, 52, 86, 0.82)", "rgba(74, 185, 240, 0.82)","rgba(48, 145, 222, 0.82)", "rgba(136, 58, 221, 0.82)","rgba(238, 193, 80, 0.82)"],
        data: pie_values
      }]
    };

    var options = {
      title: {
        display: true,
        text: title,
        position: 'top'
      },
      rotation: -0.7 * Math.PI,
      hover: {
        animationDuration: 0
      },
      animation: {
        onComplete: function () {
          // var chartInstance = this.chart;
          var chartInstance = this;
          var ctx = chartInstance.chart.ctx;
          chartInstance.data.datasets.forEach(function(dataset, i) {
            var meta = chartInstance.getDatasetMeta(i);
            if (!meta.hidden) {
              meta.data.forEach(function(element, index) {
                // Draw the text in black, with the specified font
                ctx.fillStyle = 'black';
                var fontSize = 16;
                var fontStyle = 'normal';
                var fontFamily = 'Helvetica Neue';
                ctx.font = Chart.helpers.fontString(fontSize, fontStyle, fontFamily);
                // Just naively convert to string for now
                var dataString = dataset.data[index].toString();
                // Make sure alignment settings are correct
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                var padding = 5;
                var position = element.tooltipPosition();
                ctx.fillText(dataString + '%', position.x, position.y - (fontSize / 2) - padding);


              });
            }
          });
        }
      },

      legend: {
        display: true,
        labels: {
          generateLabels: function(chart) {
            var data = chart.data;
            if (data.labels.length && data.datasets.length) {
              return data.labels.map(function(label, i) {
                var meta = chart.getDatasetMeta(0);
                var ds = data.datasets[0];
                var arc = meta.data[i];
                var custom = arc && arc.custom || {};
                var getValueAtIndexOrDefault = theHelp.getValueAtIndexOrDefault;
                var arcOpts = chart.options.elements.arc;
                var fill = custom.backgroundColor ? custom.backgroundColor : getValueAtIndexOrDefault(ds.backgroundColor, i, arcOpts.backgroundColor);
                var stroke = custom.borderColor ? custom.borderColor : getValueAtIndexOrDefault(ds.borderColor, i, arcOpts.borderColor);
                var bw = custom.borderWidth ? custom.borderWidth : getValueAtIndexOrDefault(ds.borderWidth, i, arcOpts.borderWidth);
                  return {
                  // And finally :
                  text:label,
                  fillStyle: fill,
                  strokeStyle: stroke,
                  lineWidth: bw,
                  hidden: isNaN(ds.data[i]) || meta.data[i].hidden,
                  index: i
                };
              });
            }
            return [];
          }
        }
      }
    };

    // Chart declaration:
    var myPieChart = new Chart(ctx2, {
      type: 'pie',
      data: data,
      options: options
    });

  // part for bar chart
  ctx = document.getElementById("bar-chart");

  ctx.style.backgroundColor="#fff";



  new Chart(ctx, {
    type: 'bar',

    data: {
      labels: label,
      datasets: [
        {
          label: label,
          backgroundColor: ["rgba(48, 145, 222, 0.82)", "rgba(136, 58, 221, 0.82)","rgba(238, 193, 80, 0.82)","rgba(240, 87, 207, 0.82)","rgba(247, 135, 239, 0.82)","rgba(238, 52, 86, 0.82)", "rgba(74, 185, 240, 0.82)","rgba(48, 145, 222, 0.82)", "rgba(136, 58, 221, 0.82)","rgba(238, 193, 80, 0.82)"],
          data: values
        }
      ]
    },
    options: {
      legend: { display: false },
      hover: {
        animationDuration: 0
      },
      animation: {
        onComplete: function () {
          var chartInstance = this.chart;
          var ctx = chartInstance.ctx;
          ctx.font = Chart.helpers.fontString(Chart.defaults.global.defaultFontSize, Chart.defaults.global.defaultFontStyle, Chart.defaults.global.defaultFontFamily);
          ctx.fillStyle = "black";
          ctx.textAlign = 'center';
          ctx.textBaseline = 'bottom';

          this.data.datasets.forEach(function (dataset, i) {
            var meta = chartInstance.controller.getDatasetMeta(i);
            meta.data.forEach(function (bar, index) {
                var data = dataset.data[index];
                ctx.fillText(data, bar._model.x, bar._model.y - 5);
            });
          });
        }
      },
      title: {
        display: true,
        text: title,
        fontSize:20
      },
      layout: {
            padding: {
                left: 20,
                right: 20,
                top: 0,
                bottom: 0
            }
        },
      scales: {
        yAxes : [{
            ticks : {

                min : 0,
                max : max_value+1,
                userCallback: function(label, index, labels) {
                  if (Math.floor(label) === label) {
                  return label;
                  }

                },
            }
        }]
      }

    }
  });
});

function hasDuplicates(array) {
    var valuesSoFar = Object.create(null);
    for (var i = 0; i < array.length; ++i) {
        var value = array[i];
        if (value in valuesSoFar) {
            return true;
        }
        valuesSoFar[value] = true;
    }
    return false;
}


function create_movie_poll(){
  console.log("function starts");
  var poll_name = $("#poll_name").val();
  var options = document.getElementsByClassName('poll-option');
  var description = $("#poll_description").val();
  var category = $("#category").val();
  var options_list =[];
  for (var i=0; i<options.length;i++){
    options_list.push(options[i].value);
  }

  var poll_name_check = poll_name.search(/[^A-Za-z0-9\s\(\)-?\.!]/ig);
  if(poll_name_check>=0){
    alert("The poll name is invalid!");
    return;
  }

  for ( i=0;i<options_list.length;i++){
    var option_check = options_list[i].search(/[^A-Za-z0-9\s\(\):\'\.]/ig);
    if(option_check>=0){
      alert(options_list[i]+" is illegal!");
      return;
    }
    if(options_list[i].length>50){
      alert("The length of "+options_list[i]+" is too long!");
      return;
    }

  }

  var description_check = description.search(/[^A-Za-z0-9\s\(\),\.!\"\?!-\']/ig);
  if(description_check>=0){
    alert("The description is invalid!");
    console.log("The description is invalid!");
    return;
  }

  if(poll_name==""){
    alert("The poll name is empty!");
    return;
  }

  if(options.length<2 ){
    alert("The options are less than 2");
    return;
  }

  if(options.length>10){
    alert("The options are more than 10");
    return;
  }

  if(hasDuplicates(options_list)){
    alert("Duplicate options exist");
    return;
  }

  if(category==""){
    alert("The category is empty");
    return;
  }
  var options_string = options_list.join(',');
  console.log("Before ajax sending");
  $.ajax({
    data : {
      poll_name : poll_name,
      options: options_string,
      category:category,
      description:description
    },
    type : 'POST',
    url : '/create_poll_submit'
  })
  .done(function(data) {

    if (data.error) {
      $('#errorAlert').text(data.error).show();
    }
    else{
      console.log("Success");
      window.location = "/index";
    }
  });

  event.preventDefault();
}
