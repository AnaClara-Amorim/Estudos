function carregar() {
    //Criação de objetos
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
   
    msg.innerHTML = (`Agora são ${hora} horas.`)

    if (hora >= 0 && hora <= 12) {
        //Bom dia. Usando o objeto img vamos carregar a imagem aqui
        img.src = 'fotomanha.png'
        document.body.style.background = '#fce48d' //Aqui usado para mudar a cor do fundo
    } else if (hora >= 12 && hora < 18) { 
        //Boa tarde
        img.src = 'fototarde.png'
        document.body.style.background = '#feb142'
    } else {
        //Boa noite
        img.src = 'fotonoite.png'
        document.body.style.background = '#546691'
    }
} //Depois da criação desta function, coloca-se o onload no body