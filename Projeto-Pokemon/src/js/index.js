/* Objetivo 1 - Ao clicar no botão de troca de tema, adicionar a classe modo-escuro no body para que os estilos do modo escujo sejam aplicados e mudar a imagem pra lua

- passo 1 - pegar no js o elemento html correspondente  ao botao de troca de tema
- passo 2 - pegar no js o elemento html correspondente ao body 
- passo 3 - identificar o clique do usuário no botão de troca de tema
- passo 4 - adicionar a classe modo escuro no body 
- passo 5 - trocar a imagem do botão de alterar tema para lua 

Objetivo 2 - quando clicar no botão de trocad de tema, caso o body ja tenha a classe modo-escuro, remover a classe para mudar para modo claro e mudar a imagem para sol
- passo 6 - verificar se o body já tem a classe modo-escuro
- passo 7 - remover a classe do modo escuro do body 
- passo 8 - trocar a imagem do botão de alterar tema para sol */

// passo 1 - pegar no js o elemento html correspondente  ao botao de troca de tema

const botaoAlterarTema = document.getElementById("botao-alterar-tema");

// passo 2 - pegar no js o elemento html correspondente ao body 

const body = document.querySelector("body");

//4.1 adicionando constante para alterar sol paralua

const imagemBotaoTrocaDeTema =  document.querySelector(".imagem-botao")

// passo 3 - identificar o clique do usuário no botão de troca de tema

botaoAlterarTema.addEventListener("click",() => {

    /* Objetivo 2 - quando clicar no botão de trocad de tema, caso o body ja tenha a classe modo-escuro, remover a classe para mudar para modo claro e mudar a imagem para sol */
    //passo 6 - verificar se o body já tem a classe modo-escuro
    const modoEscuroEstaAtivo = body.classList.contains("modo-escuro")
    
    if (modoEscuroEstaAtivo){
        //passo 7 - remover a classe do modo escuro do body 
        body.classList.remove("modo-escuro");
        //passo 8 - trocar a imagem do botão de alterar tema para sol
        imagemBotaoTrocaDeTema.setAttribute("src", "./src/imagens/sun.png")

    } else {
        // passo 4 - adicionar a classe modo escuro no body 
    body.classList.add("modo-escuro");

    // passo 5 - trocar a imagem do botão de alterar tema para lua
    imagemBotaoTrocaDeTema.setAttribute("src", "./src/imagens/moon.png")
  }   
}); // arrow function 