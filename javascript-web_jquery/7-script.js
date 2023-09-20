// prevent jQuery code running before document is loaded
$(document).ready(function () {
  // save the url into a const
  const apiURL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  // use the .get() method to fetch the data/character name
  $.get(apiURL, function (data) {
    // save the name of the character
    const charName = data.name;
    // get the place to put the character name
    const charPlace = $('div#character');
    // set the div with he character's name
    $(charPlace).text(charName);
  });
});
