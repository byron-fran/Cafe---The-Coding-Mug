const btnAdd = document.querySelector("#btn_add");
const quantity = document.querySelector("#quantity")
const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;

btnAdd.addEventListener('click', async () => {
    const quantityMenu = quantity.value 
    await addQuantity(quantityMenu)       
})


async function addQuantity (q){
  fetch(`http://localhost:8000/Menu/menu/add/`, {
        body : {
           image : 'https://res.cloudinary.com/dtvbans9e/image/upload/v1/media/menu/coffee-842020_1280_pcmutu',
           price : 200,
           name : 'Cafe italiano',
           description : 'istraerá con el contenido del texto de un sitio mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal de las letras, al contrario de usar textos como por ejemplo "Contenido aquí, contenido aquí". Estos textos hacen parecerlo un español que se puede leer. Muchos paquetes de autoedición y editores de páginas web usan el Lorem Ipsum como su texto por defecto, y al hacer una búsqueda de "Lorem Ipsum" va a dar por resultado muchos sitios web que usan este texto si se encuentran en estado de desarrollo. Muchas versiones han evolucionado a través de los a',
           slug : 'Cafe_italiano'
        },
        method : "POST",
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrfToken  // Especificar el tipo de contenido JSON
            // Puedes incluir otros encabezados si es necesario
        },
    

    }).then(res => {
        console.log(res)
    })
    .catch(error => {
        console.log(error)
    })
}