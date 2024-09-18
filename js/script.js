//
//  オーソドックスな関数定義
//
function FuncA()
{
    console.log("FuncA");
}

//
//  無名関数定義
//
const FuncB = function () {
    console.log("FuncB");
}

//
//  ラムダ式
//
const FuncC = () => {
    console.log("FuncC");
}

//
//  ラムダ式引数
//
const FuncD = (d) => {
    console.log(`FuncD${d}`);
}

//
//  ラムダ式引数に関数をもらう
//
const FuncE = (e) => {
    e();
}



FuncA();        //  オーソドックスな関数定義呼び出し
FuncB();        //  無名関数呼び出し
FuncC();        //  ラムダ式呼び出し
FuncD(123);     //  ラムダ式引数付き呼び出し
FuncE( () => { console.log("FuncE"); } );        //  ラムダ式引数に関数を渡して呼び出し
