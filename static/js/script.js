// Función para cargar la lista de pacientes desde el backend
function cargarPacientes() {
    fetch('/pacientes', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(pacientes => {
        const listaPacientes = document.getElementById('pacientes-lista');
        listaPacientes.innerHTML = ''; // Limpiar lista antes de agregar los nuevos pacientes
        
        pacientes.forEach(paciente => {
            const li = document.createElement('li');
            li.textContent = `${paciente.nombre} ${paciente.apellido} - ${paciente.numero_identificacion}`;
            listaPacientes.appendChild(li);
        });
    })
    .catch(error => {
        console.error('Error al cargar los pacientes:', error);
    });
}

// Función para manejar el envío del formulario
const formPaciente = document.getElementById('form-paciente');

formPaciente.addEventListener('submit', function(event) {
    event.preventDefault(); // Evita la recarga de la página

    // Captura los datos del formulario
    const pacienteData = {
        nombre: document.getElementById('nombre').value,
        apellido: document.getElementById('apellido').value,
        fecha_nacimiento: document.getElementById('fecha_nacimiento').value,
        genero: document.getElementById('genero').value,
        numero_identificacion: document.getElementById('numero_identificacion').value
    };

    // Enviar datos con Fetch API
    fetch('/pacientes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(pacienteData)
    })
    .then(response => response.json()) // Convierte la respuesta a JSON
    .then(data => {
        alert('Paciente guardado con éxito!');
        console.log(data); // Muestra los datos recibidos

        // Volver a cargar la lista de pacientes
        cargarPacientes();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Hubo un error al guardar el paciente.');
    });
});

// Función para manejar la búsqueda de pacientes
const formBusqueda = document.getElementById('form-busqueda');

formBusqueda.addEventListener('submit', function(event) {
    event.preventDefault(); // Evita la recarga de la página
    
    const criterio = document.getElementById('buscar-criterio').value;
    const valor = document.getElementById('buscar-valor').value;

    if (valor) {
        fetch(`/pacientes/buscar?${criterio}=${valor}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            const resultadoBusqueda = document.getElementById('resultado-busqueda');
            if (data.message) {
                resultadoBusqueda.innerHTML = `<p>${data.message}</p>`;
            } else {
                resultadoBusqueda.innerHTML = `
                    <h3>Paciente(s) Encontrado(s):</h3>
                    <ul>
                        ${data.map(paciente => `
                            <li>${paciente.nombre} ${paciente.apellido} - ${paciente.numero_identificacion}</li>
                        `).join('')}
                    </ul>
                `;
            }
        })
        .catch(error => {
            console.error('Error al buscar el paciente:', error);
            alert('Hubo un error al buscar el paciente.');
        });
    } else {
        alert('Por favor, ingresa un valor para buscar.');
    }
});

// Cargar la lista de pacientes al cargar la página
window.addEventListener('DOMContentLoaded', cargarPacientes);
