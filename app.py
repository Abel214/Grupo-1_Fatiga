const boton = document.getElementById("startButton");
const selector = document.getElementById("cameraSelect");
const audioCansancio = new Audio("/static/sounds/cansancio.mp3");
const audioSomnolencia = new Audio("/static/sounds/somnolencia.mp3");
const ear = document.getElementById("ear");
const mar = document.getElementById("mar");
let ultimoEstado = "ALERTA";

boton.addEventListener("click", async () => {

    const camara =
        document.getElementById("cameraSelect").value;

    await fetch("/start/" + camara);

    document.getElementById("video").src =
        "/video";
});

const estado=document.getElementById("estado");

function cambiarEstado(nuevo){

    estado.className="";

    if(nuevo==="ALERTA"){

        estado.classList.add("alerta");

    }

    if(nuevo==="CANSANCIO"){

        estado.classList.add("cansancio");

    }

    if(nuevo==="SOMNOLENCIA"){

        estado.classList.add("somnolencia");

    }

    estado.innerHTML=nuevo;

}

// Solo para probar la interfaz

async function actualizarEstado(){

    try{

        const respuesta = await fetch("/estado");

        const datos = await respuesta.json();
        
        console.log(datos);

        cambiarEstado(datos.estado);

        ear.textContent = datos.ear.toFixed(3);

        mar.textContent = datos.mar.toFixed(3);

    }

    catch(error){

        console.log(error);

    }

}

async function cargarCamaras(){

    const respuesta = await fetch("/camaras");

    const datos = await respuesta.json();

    selector.innerHTML = "";

    datos.camaras.forEach(numero => {

        const opcion = document.createElement("option");

        opcion.value = numero;

        opcion.textContent = "Cámara " + numero;

        selector.appendChild(opcion);

    });

}

cargarCamaras();

actualizarEstado();

setInterval(actualizarEstado,300);