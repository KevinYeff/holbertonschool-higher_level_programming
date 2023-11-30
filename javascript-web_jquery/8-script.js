// prevent jQuery code running before document is loaded
$(document).ready(function () {
  // get the element that will contain the list
  const ulElement = $('#list_movies');
  const apiURL = 'https://swapi-api.hbtn.io/api/films/?format=json';

  // Use jQuery .get() method to fetch the data
  $.get(apiURL, function (fetchData) {
    // get an array of the movie objects from the JSON
    const listOfMovies = fetchData.results;
    // iterate through the array
    listOfMovies.forEach(function (movie) {
      // keep the movie title for each iteration
      const movieTitle = movie.title;
      // create a list item for the current movie title and append it to the ul element
      const listItem = $('<li>').text(movieTitle);
      ulElement.append(listItem);
    });
  });
});
