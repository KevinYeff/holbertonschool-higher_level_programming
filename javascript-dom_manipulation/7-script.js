// get the element that will contain the list
const ul_element = document.getElementById('list_movies');
//URL
const apiURL = 'https://swapi-api.hbtn.io/api/films/?format=json'

// fetch
fetch(apiURL)
    .then(function(the_json){
        //the json
        return the_json.json();
    })
    .then(function(list_of_movies){
        //get an array of the objects from the json
        const title_of_movies = list_of_movies.results;
        //console.log(title_of_movies);
        //iterate through the array
        title_of_movies.forEach(function(movie) {
            //keep the movie title each ieration
            const movie_title = movie.title;
            //console.log(movie_title);
            //create a list inside the ul element for aesthethics
            const list_movie_title = document.createElement('li');
            //set every li iwth the current title in the iteration
            list_movie_title.textContent = movie_title;
            //ul_element.append(movie_title);
            //append the li for the ul element in each iteration
            ul_element.appendChild(list_movie_title);
        });
    });
