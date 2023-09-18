//updates the text color of the header
const header = document.querySelector('header');
//only whe user click in this tag
const change_to_red = document.getElementById('red_header');
//I use the listener to apply the behaviour
change_to_red.addEventListener('click', function(){
    header.style.color = '#FF0000';
});
