
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

    $(document).ready(function() {
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
          title: {
            display: true,
            text: title
          },
          scales: {
                yAxes : [{
                    ticks : {

                        min : 0
                    }
                }]
            }

        }
    });

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
  console.log("Poll name here");
  var options = document.getElementsByClassName('poll-option');
  var category = $("#category").val();
  var options_list =[];
  for (var i=0; i<options.length;i++){
    options_list.push(options[i].value);
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
      category:category
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
