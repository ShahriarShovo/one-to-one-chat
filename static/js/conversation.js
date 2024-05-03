

let loc = window.location
let wsStart = 'ws://'

if(loc.protocol === 'http') {
    wsStart = 'wss://'
}
let endpoint = wsStart + loc.host + loc.pathname

var socket = new WebSocket(endpoint)


socket.onopen = async function(e){
    console.log('open', e)
    
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






