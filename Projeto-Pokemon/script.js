function alternarModoEscuro() {
    var bodyElement = document.body;
    var cartaoPokemonElements = document.querySelectorAll('.cartao-pokemon');

    bodyElement.classList.toggle('modo-escuro');

    cartaoPokemonElements.forEach(function(element) {
        element.classList.toggle('cartao-hover');
    });
}