const asyncFunc = async () => {
    console.log("処理A");
    
    await new Promise( (resolve) => {
        setTimeout( () => {
            console.log("処理F");
            resolve();
        }, 1000);
    });
    
    console.log("処理G")
}

asyncFunc();