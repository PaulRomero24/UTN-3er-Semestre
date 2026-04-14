"use strict";

// En modo estricto, no se pueden usar variables sin declararlas
// Esto ayuda a evitar errores comunes y mejora la seguridad del código

const x = 10; // Esto es correcto
console.log(x);

miFuncion(); // Esto causará un error porque miFuncion no está definida
function miFuncion() {
    let y = 20; // Esto es correcto
    console.log(y);
}
