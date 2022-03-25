// THIS FINE DOES NOT WORK, WE NEED TO REMOVE THE PIPE FILES SOMEHOW WHEN THE PROCESS EXITS!!!

process.stdin.resume();//so the program will not close instantly

function exitHandler(options:any, exitCode:number) {
    console.log("heeyyyyy")
    console.log(options)
    if (options.cleanup) console.log('clean');
    if (exitCode || exitCode === 0) console.log(exitCode);
    if (options.exit) process.exit();
    process.exit()
}

//do something when app is closing
process.on('exit', exitHandler.bind(null,{cleanup:true}));

//catches ctrl+c event
process.on('SIGINT', exitHandler.bind(null, {exit:true}));

// catches "kill pid" (for example: nodemon restart)
process.on('SIGUSR1', exitHandler.bind(null, {exit:true}));
process.on('SIGUSR2', exitHandler.bind(null, {exit:true}));

//catches uncaught exceptions
process.on('uncaughtException', exitHandler.bind(null, {exit:true}));