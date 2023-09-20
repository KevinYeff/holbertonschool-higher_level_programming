// prevent jQuery code running before document is loaded
$(document).ready(function () {
  // get the elements to work to
  const helloId = $('div#hello');
  // URL
  const apiURL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(apiURL, function (importingHello) {
    // get the hello word
    const helloWord = importingHello.hello;
    // fill the div with the word
    helloId.text(helloWord);
  });
});
