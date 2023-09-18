// https://stackoverflow.com/questions/5704924/
window.onload = function() {
    // console.log("DOM fully loaded");
    // getting the element with id hello
    const hello_id = document.getElementById('hello')
    //URL
    apiURL = 'https://hellosalut.stefanbohacek.dev/?lang=fr'

    fetch(apiURL)
        .then(function(importing_hello){
            //get the json
            return importing_hello.json();
        })
        .then(function(hello_to_display){
            // get the hello word
            const hello_word = hello_to_display.hello;
            //fill the div with the word
            hello_id.textContent = hello_word;
        });
};
