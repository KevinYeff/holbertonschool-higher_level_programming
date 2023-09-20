// prevent jQuery code running before document is loaded
$(document).ready(function () {
  // get the elements to work to
  const updateScript = $('div#toggle_header');
  const textToUpdate = $('header');
  // const redClass = 'red';
  // const greenClass = 'green';
  $(updateScript).click(function () {
    textToUpdate.toggleClass('red green');
  });
});
