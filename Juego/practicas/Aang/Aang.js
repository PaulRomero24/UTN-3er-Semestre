let ataqueJugador
let ataqueEnemigo
const ataques = ["puño", "patada", "barrida", "cubrirse"];

function iniciarJuego() {
    let botonSeleccionar = document.getElementById("boton-personaje");
    botonSeleccionar.addEventListener("click", seleccionarPersonaje);
    document.getElementById("boton-reiniciar")
    .addEventListener("click", reiniciar);

    // cada botón llama a combate() con su ataque
    document.getElementById("boton-punio")
        .addEventListener("click", () => combate("puño"));
    document.getElementById("boton-patada")
        .addEventListener("click", () => combate("patada"));
    document.getElementById("boton-barrida")
        .addEventListener("click", () => combate("barrida"));
    document.getElementById("boton-sumision")
        .addEventListener("click", () => combate("cubrirse"));


}
function seleccionAleatioriaEnemigo() {
    let enemigoSeleccionado = document.getElementById("enemigo-seleccionado");
    let enemigos = ["Azula", "Ozai", "Combustion"];
    let enemigoAleatorio = enemigos[Math.floor(Math.random() * enemigos.length)];
    enemigoSeleccionado.innerHTML = enemigoAleatorio;
}

function seleccionarPersonaje() {
//MODIFICACION DE CODIGO PARA MEJOR LEGIBILIDAD
//Declaramos variables para cada personaje
    let inputAang = document.getElementById("aang");
    let inputKatara = document.getElementById("katara");
    let inputZuko = document.getElementById("zuko");
    let inputToph = document.getElementById("toph");
    let personajeSeleccionado = document.getElementById("personaje-seleccionado");
//Verificamos cuál personaje ha sido seleccionado y mostramos el mensaje correspondiente
    if (inputAang.checked) {
        personajeSeleccionado.innerHTML = "Aang";
        alert("Has seleccionado a Aang");
    } else if (inputKatara.checked) {
        personajeSeleccionado.innerHTML = "Katara";
        alert("Has seleccionado a Katara");
    } else if (inputZuko.checked) {
        personajeSeleccionado.innerHTML = "Zuko";
        alert("Has seleccionado a Zuko");
    } else if (inputToph.checked) {
        personajeSeleccionado.innerHTML = "Toph";
        alert("Has seleccionado a Toph");
    } else {
        alert("Por favor, selecciona un personaje");
    }

    if (inputAang.checked || inputKatara.checked || inputZuko.checked || inputToph.checked) {
        seleccionAleatioriaEnemigo();
    }

}
//--------------COMBATE---------------
function combate(ataqueElegido) {
    // ataque aleatorio del enemigo
    let ataqueEnemigoElegido = ataques[Math.floor(Math.random() * ataques.length)];

    // guardamos en las variables globales
    ataqueJugador = ataqueElegido;
    ataqueEnemigo = ataqueEnemigoElegido;

    // leemos las vidas actuales del HTML
    let vidasJugador = parseInt(document.getElementById("vidas-jugador").innerHTML);
    let vidasEnemigo = parseInt(document.getElementById("vidas-enemigo").innerHTML);

    // determinamos quién gana el round
    let resultado = determinarGanador(ataqueJugador, ataqueEnemigo);

    // mostramos el mensaje
    let mensaje = document.getElementById("mensaje-ataque");
    mensaje.innerHTML = ` ${ataqueJugador} | Enemigo: ${ataqueEnemigo} → `;

    if (resultado === "jugador") {
        vidasEnemigo--;
        mensaje.innerHTML += "¡Ganaste el round!";
    } else if (resultado === "enemigo") {
        vidasJugador--;
        mensaje.innerHTML += "¡Perdiste el round!";
    } else {
        mensaje.innerHTML += "¡Empate!";
    }

    // actualizamos las vidas en el HTML
    document.getElementById("vidas-jugador").innerHTML = vidasJugador;
    document.getElementById("vidas-enemigo").innerHTML = vidasEnemigo;

    // verificamos si alguien llegó a 0
    if (vidasJugador <= 0) {
        alert(" — ¡GAME OVER! Perdiste 😔")
        desactivarBotones();
    } else if (vidasEnemigo <= 0) {
        alert(" — ¡GANASTE! 🏆")
        desactivarBotones();
    }
}
function determinarGanador(jugador, enemigo) {
    if (jugador === "cubrirse" || enemigo === "cubrirse") {
        return "empate"; // cubrirse bloquea siempre
    }
    if (jugador === enemigo) {
        return "empate";
    }
    if (
        (jugador === "punio"    && enemigo === "barrida") ||
        (jugador === "patada"  && enemigo === "punio") ||
        (jugador === "barrida" && enemigo === "patada")
    ) {
        return "jugador";
    }
    return "enemigo";
}

function desactivarBotones() {
    document.getElementById("boton-punio").disabled    = true;
    document.getElementById("boton-patada").disabled   = true;
    document.getElementById("boton-barrida").disabled  = true;
    document.getElementById("boton-sumision").disabled = true;
}

function reiniciar() {
    // resetear vidas
    document.getElementById("vidas-jugador").innerHTML = 3;
    document.getElementById("vidas-enemigo").innerHTML = 3;

    // busca todos los radio buttons de una vez y los desmarca
    document.querySelectorAll('input[name="personaje"]').forEach(function(radio) {
    radio.checked = false;
});

    // limpiar nombres
    document.getElementById("personaje-seleccionado").innerHTML = "";
    document.getElementById("enemigo-seleccionado").innerHTML   = "";

    // limpiar mensaje
    document.getElementById("mensaje-ataque").innerHTML = "";

    // reactivar botones de ataque
    document.getElementById("boton-punio").disabled    = false;
    document.getElementById("boton-patada").disabled   = false;
    document.getElementById("boton-barrida").disabled  = false;
    document.getElementById("boton-sumision").disabled = false;
}

window.addEventListener("load", iniciarJuego);