// geting the element with id 'character'
const character_element = document.getElementById('character');

// URL
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Realizar una solicitud GET utilizando la Fetch API
fetch(apiUrl)
  .then(function(the_json) {
    // get the JSON
    return the_json.json();
  })
  .then(function(character_in_json) {
    // get the name of the character from json
    const character_name = character_in_json.name;

    // fill the blank space with the character's name
    character_element.textContent = character_name;
  });
