// prevent jQuery code running before document is loaded
$(document).ready(function () {
  // getting the elements to work to
  const updateOnClick = $('header');
  const scriptElement = $('div#red_header');
  $(scriptElement).click(function () {
    updateOnClick.css('color', '#FF0000');
  });
});
