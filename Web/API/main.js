console.log('Hola mundo');

const URL = "https://platzi-store.herokuapp.com/cart"
// query parameter ?
const URL2 = "https://api.thecatapi.com/v1/images/search?limit=3";
// URL2 tiene un QUERY limit (limite de imagenes) y page(pagina a cargar)

// Devuelven una promesa
// fetch(URL)
//     .then(response => {
//         return response.json()
//     })
//     .then(data => {
//         console.log(data)
//     })

// fetch(URL)
//     .then(response => response.json())
//     .then(data => {
//         const img = document.querySelector("img")
//         img.src = data.cart.products[0].picture
//         // data[0].url
//     })

async function getCat() {
    const response = await fetch(URL2);
    const data = await response.json();
    const img1 = document.getElementById("img1");
    const img2 = document.getElementById("img2");
    const img3 = document.getElementById("img3");
    img1.src = data[0].url;
    img2.src = data[1].url;
    img3.src = data[2].url;
}
getCat()