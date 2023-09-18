//getting the tag
const update_header_on_click = document.getElementById('update_header');
//add even listener
update_header_on_click.addEventListener('click', function(){
    //updates de text of the header element to New Header!!! 
    const header = document.querySelector('header');
    //changes the text
    header.textContent = 'New Header!!!';
});
