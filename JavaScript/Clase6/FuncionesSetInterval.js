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


//funcion de tipo callback con setInterval
let reloj = setInterval(function() {
    let fecha = new Date();
    console.log(`La hora actual es: ${fecha.toLocaleTimeString()}`);
}, 1000); // El mensaje se mostrará cada 1000 milisegundos (1 segundo)

// Para detener el reloj después de 10 segundos 
setTimeout(function() {
    clearInterval(reloj);
    console.log("El reloj se ha detenido");
}, 10000); // El reloj se detendrá después de 10000 milisegundos (10 segundos)