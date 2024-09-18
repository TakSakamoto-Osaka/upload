console.log("処理A");

/*
const promise = new Promise( (resolve) => {
    setTimeout(() => {
        console.log("処理B");
        resolve();
    }, 1000);
});

promise.then( () => {
    console.log("処理C")
} );
*/

const promise = new Promise( (resolve) => {
    setTimeout( () => {
        console.log("処理D");
        resolve();
    }, 1000 );
} ).then( () => {
    console.log("処理E");
} );
