let botao = document.querySelector("#botao");
let estaRoxo = false;

botao.style.background="blue";

//if (!estaRoxo){
botao.addEventListener("mouseover", trocaVerde)

    function trocaVerde() {
        botao.style.background = "green";
    } 
    
    botao.addEventListener("mouseout", trocaAzul)
    
    function trocaAzul() {
        botao.style.background = "blue";
    }   




botao.addEventListener("click", trocaPurple);

function trocaPurple() {
    botao.style.background = "purple"
    botao.innerHTML = "Puuuurple"
    estaRoxo=true
}