// prevent jQuery code running before document is loaded
$(document).ready(function () {
  // get the elements to work to
  const updateScript = $('div#red_header');
  const textToUpdate = $('header');
  const classToAdd = 'red';
  // add the event
  $(updateScript).click(function () {
    // using the addclass() method
    textToUpdate.addClass(classToAdd);
  });
});
