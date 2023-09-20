// prevent jQuery code running before document is loaded
$(document).ready(function () {
  // get the elements to work to
  const addItemScript = $('div#add_item');
  const ulList = $('ul.my_list');
  // select the div with id "add_item" and add a click event handler
  $(addItemScript).click(function () {
    // create a new li element with the text "Item"
    const newItem = $('<li>Item</li>');
    // append the new li element to the ul with class "my_list"
    $(ulList).append(newItem);
  });
});
