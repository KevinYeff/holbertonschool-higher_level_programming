//getting the elements
const header = document.querySelector('header');
const change_to_red = document.getElementById('red_header');
//aplying changes 
change_to_red.addEventListener('click', function(){
    //add a class to the header classlist
    header.classList.add('red');
});
