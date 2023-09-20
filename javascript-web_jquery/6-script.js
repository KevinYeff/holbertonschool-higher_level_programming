// prevent jQuery code running before document is loaded
$(document).ready(function () {
  // get the elements to work to
  const updateHeader = $('div#update_header');
  // use the event
  $(updateHeader).click(function () {
    const headerToUpdate = $('header');
    headerToUpdate.text('New Header!!!');
  });
});
