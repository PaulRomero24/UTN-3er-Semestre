//funcion de tipo callback
function imprimir(mensaje) {
    console.log(mensaje);
}
function sumar (a, b, callback) {
    let resultado = a + b;
    callback(`El resultado de la suma es: ${resultado}`);
}
sumar(5, 10, imprimir);


//funcion de tipo callback con setTimeout
function mostrarMensaje() {
    console.log("Este mensaje se muestra después de 2 segundos");
}
setTimeout(mostrarMensaje, 2000); // El mensaje se mostrará después de 2000 milisegundos (2 segundos)

//Otra forma de usar setTimeout con una función anónima
setTimeout(function() {
    console.log("Este mensaje se muestra después de 3 segundos");
}, 3000); // El mensaje se mostrará después de 3000 milisegundos (3 segundos)