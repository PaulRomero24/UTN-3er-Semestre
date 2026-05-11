function Funcion1() {
    console.log("Funcion 1");
}

function Funcion2() {
    console.log("Funcion 2");
}

//funcion de tipo callback
function imprimir(mensaje) {
    console.log(mensaje);
}


//Aca asignamos una variable a una funcion.

//let imp function imprimir = function(mensaje) {
//    console.log(mensaje);
//}

function sumar (a, b, callback) {
    let resultado = a + b;
    callback(`El resultado de la suma es: ${resultado}`);
}
sumar(5, 10, imprimir);