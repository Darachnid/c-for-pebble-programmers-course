/* Phone side starter: complete the message handshake yourself. */
Pebble.addEventListener('ready',function(){console.log('Field Guide phone ready');});
Pebble.addEventListener('appmessage',function(e){console.log(JSON.stringify(e.payload));/* TODO: Pebble.sendAppMessage */});
