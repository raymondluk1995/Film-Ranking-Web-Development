var login_status =0;
var display_user_name = "  ";
var user = "";

function log_out_show(){
  var logout_part = document.getElementById('logout-part');
  logout_part.style.display = "block";
}



function close_window(event){
  event.target.parentNode.parentNode.style.display = 'none';
}

function hide_all_outer_div(){
  var html_div = document.getElementsByClassName('outer');
  for (var i=0; i<html_div.length;i++){
    html_div[i].style.display = "none";
  }
}

function log_in_out(){
  if(login_status==0){
    var login_part = document.getElementById('login-part');
    hide_all_outer_div();
    login_part.style.display = "block";
  }
  if(login_status==1){
    var logout_part = document.getElementById('logout-part');
    logout_part.style.display = "block";
  }
}

function sign_in(){
  var html_login_form = document.getElementById('loginForm');
  if(html_login_form.elements["form-username"].value==""||html_login_form.elements["form-password"].value==""){
    alert("Username and password cannot be blank!!");
    return;
  }
  user = html_login_form.elements["form-username"].value.toString();
  var password = html_login_form.elements["form-password"].value;
  display_user_name += user.slice(0,3);
  var nav_user_p = document.getElementById('nav-user-a');
  nav_user_p.innerHTML += display_user_name;
  login_status = 1;
  document.getElementById('login-part').style.display = "none";

}

function sign_out(event){
  user = "";
  var nav_user_a = document.getElementById('nav-user-a');
  var regex = new RegExp(display_user_name,"g");
  nav_user_a.innerHTML=nav_user_a.innerHTML.replace(regex,"");
  display_user_name = "  ";
  login_status =0;
  event.target.parentNode.parentNode.style.display = 'none';
  console.log(login_status);
}

function register(){
  hide_all_outer_div();
  document.getElementById('register-part').style.display="block";
}


function finish_register(){
  var html_register_form = document.getElementById('registerForm');
  console.log(html_register_form.elements['username'].value);

  if(html_register_form.elements["username"].value==""||html_register_form.elements["password"].value==""||html_register_form.elements["confirm-password"].value==""||html_register_form.elements["email"].value==""){
    alert("All blanks must be filled!");
    return;
  }

  if(html_register_form.elements["username"].value.toString().length<4){
    alert("The length of username is less than 4 characters!");
    return;
  }

  if(html_register_form.elements["password"].value!=html_register_form.elements["confirm-password"].value){
    alert("Password is different from the confirm password!");
    return;
  }

  var email_regex = /^(\w+)@([\.|\w]+)\.(\w){2,4}$/;
  if(html_register_form.elements["email"].value.toString().match(email_regex)==null){
    alert("You insert an invalid email!");
    return;
  }

  var html_checkbox = document.getElementsByClassName('checkbox');
  var checkbox_choice =[];
  for (var i=0; i<html_checkbox.length;i++){
    if(html_checkbox[i].children[0].children[0].checked){
      checkbox_choice.push(html_checkbox[i].children[0].children[0].value);
    }
  }
  if(checkbox_choice.length==0){
    alert("Please select at least one preference!");
    return;
  }

}

// -------------The Part Cannot Be Removed----------------------
$(document).ready(function() {
    $("#Add").on("click", function() {
        $("#textboxDiv").append("<div><br>New Option :<input class='poll-option form-control' type='text' placeholder='New Option'/></div>");
    });
    $("#Remove").on("click", function() {
        $("#textboxDiv").children().last().remove();
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
  var poll_name = $("#poll_name").val();
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
