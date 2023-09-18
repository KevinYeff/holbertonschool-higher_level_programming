//getting he elements
const header = document.querySelector('header');
const toggle_header_color = document.getElementById('toggle_header');

// add the event
toggle_header_color.addEventListener('click', function(){
    //conditionals to set the behaviour using classList property contains
    if (header.classList.contains('red')){
        header.classList.remove('red');
        header.classList.add('green');
    }
    else {
        header.classList.remove('green');
        header.classList.add('red');
    }
});
