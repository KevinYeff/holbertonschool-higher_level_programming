// getting the element with id hello
const hello_id = document.getElementById('hello')
//URL
apiURL = 'https://hellosalut.stefanbohacek.dev/?lang=fr'

fetch(apiURL)
    .then(function(importing_hello){
        return importing_hello.json();
    })
    .then(function(hello_to_display){
        const hello_word = hello_to_display.hello;
        hello_id.textContent = hello_word;
    });
