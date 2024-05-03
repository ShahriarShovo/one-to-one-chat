
var textarea = document.getElementById('input_message');
console.log("Textarea element:", textarea);

let loc = window.location
let wsStart = 'ws://'

if(loc.protocol === 'https') {
    wsStart = 'wss://'
}
let endpoint = wsStart + loc.host + loc.pathname

var socket = new WebSocket(endpoint)


socket.onopen = async function(e){
    console.log('open', e)
    let value = textarea.value;
    console.log(value);
    
}

socket.onmessage = async function(e){
    console.log('onmessage', e)
    
}

socket.onerror = async function(e){
    console.log('error', e)
    
}

socket.onclose = async function(e){
    console.log('close', e)
}


console.log("Script loaded"); // Check if script is loaded

/*
document.addEventListener("DOMContentLoaded", function() {
    // Get reference to the submit button
    var submitButton = document.querySelector('.conversation-form-submit');

    // Add event listener to the submit button
    submitButton.addEventListener('click', function() {
        // Get the textarea element
        var textarea = document.getElementById('input_message');

        // Log the entire textarea element
        console.log("Textarea element:", textarea);

        // Get the text from the textarea
        var textareaValue = textarea.value;

        // Log the text to the console
        console.log("Textarea value:", textareaValue);
    });
});
*/
















