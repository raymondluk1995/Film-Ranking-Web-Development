var index =1;

//function for turning pages in the carousel
function page(num) {
  if (num == -1) {
    index--;
    if (index < 1) {
      index = 6;
    }
  }
  if (num == 1) {
    index++;
    if (index > 6) {
      index = 1;
    }
  }
  slide(index);
}

//hide all carousel pages
function hide_all(){
  var carousels = document.getElementsByClassName('carousel');
  for (var i=0; i<carousels.length;i++){
    carousels[i].style.display = "none";
  }
}

//Change the dot status when it is chosen
function change_to_active(n) {
  var all_dots = document.getElementsByClassName('dots');
  for (var i=0; i < all_dots.length; i++) {
    all_dots[i].className = all_dots[i].className.replace('active','');
  }
  all_dots[n-1].className = all_dots[n-1].className + ' active';
}

//Go to the position n carousel page
function slide(n){
  var all_slides = document.getElementsByClassName('carousel');
  hide_all();
  all_slides[n-1].style.display = 'block';
  change_to_active(n);
  index = n;
}
