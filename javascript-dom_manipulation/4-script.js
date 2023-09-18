// getting the tags (add_item and ul)
const add_item_on_click = document.getElementById('add_item');
const ul_li_to_add = document.querySelector('ul.my_list');

//creating the  event to add elements to the ul.li

add_item_on_click.addEventListener('click', function(){
    //creating the li element
    const new_element = document.createElement('li');
    //the name of the li element must be 'Item'
    new_element.textContent = 'Item';
    //add to the ul list
    ul_li_to_add.appendChild(new_element);
})
