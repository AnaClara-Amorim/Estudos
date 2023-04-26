function verificar() {
    var data = new Date ()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')

    if (fano.value.length == 0 || Number(fano.value) > ano){
        window.alert('Erro. Verifique os dados e tente novamente novamente!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        //res.innerHTML = `Idade calculada ${idade}`
        var genero = ''
        var img = document.createElement('img') //Cria uma tag img
        img.setAttribute('id', 'foto') // Como se tivesse colocado no html <img id = 'foto'>
        if (fsex[1].checked) {
            genero = 'homem'
            if (idade >=0 && idade <10) {
                //Criança
                img.setAttribute('src', 'foto-bebe-h.jpg') //Imagens de teste, não coloquei todas
            } else if (idade >=10 && idade < 21){
                // Jovem
            } else if (idade <50) {
                //Adulto
            } else {
                // Idoso
            }
        } else if (fsex[0].checked) {
            genero = 'mulher'
            if (idade >=0 && idade <10) {
                //Criança
                img.setAttribute('src', 'foto-bebe-f.jpg')
            } else if (idade >=10 && idade < 21){
                // Jovem
            } else if (idade <50) {
                //Adulto
            } else {
                // Idoso
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos de idade.`
        res.appendChild(img) //Para aparecer a imagem
    }
}

//15:40