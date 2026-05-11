
//Esto es una funcion comun
function miFuncion() {
}

miFuncion();

//Esto es una funcion de flecha o arrow function
let miFuncionFlecha = () => {
    console.log("Esto es una funcion de flecha");
}
miFuncionFlecha();
//Si la funcion de flecha tiene una sola linea de codigo, se pueden omitir las llaves y el return
let miFuncionFlecha2 = () => console.log("Esto es una funcion de flecha con una sola linea de codigo");
miFuncionFlecha2();

//EJEMPLOS de funciones de flecha
const saludar = () => console.log("Hola, soy una funcion de flecha");
saludar();

const saludar2 = () =>{
    return "Hola, soy una funcion de flecha con return";
}
console.log(saludar2());

const regresarObjeto = () => ({nombre: "Juan", edad: 30});
console.log(regresarObjeto());

//Arrow function con parametros, pero sin return
const funcionParametros = (mensaje) => mensaje;
funcionParametros("Hola, soy una funcion de flecha con parametros");

//Funcion comun con parametros y return
const funcionParametros2 = function(mensaje) {
    return mensaje;
}
console.log(funcionParametros2("Hola, soy una funcion comun con parametros"));


//Funcion flecha con varios parametros
const funcionVariosParametros = (a, b) => {
    let resultado = a + b;
    return resultado;
};
console.log(funcionVariosParametros(5, 10));