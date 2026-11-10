"use strict";

try {
    let x = 10;
    miFuncion();
}
//Esto se usa para manejar los errores que puedan surgir en el bloque de código del try,
//  evitando que el programa se detenga abruptamente.
catch (error) {
    console.log(error);
    console.log(error.name);
    console.log(error.message);
    console.log(error.stack);
}

finally {
    console.log("termina la revision de errores");
}

console.log("continuamos...");

let resultado = "hola" / 2;

try {
    if (isNaN(resultado))throw "El resultado no es un numero";
    else if (resultado === '') throw "El resultado no puede ser una cadena vacia";
    else if (resultado >= 0) throw "El resultado no puede ser un numero positivo";
}
catch (error) {
        console.log(error);
        console.log(error.name);
        console.log(error.message);
        console.log(error.stack);
        console.log(typeof error);
    }
finally {    console.log("termina la revision de errores");
}