function verificar() {
    var data = new Date ()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')

    if (fano.value.length == 0 || fano.value > ano){
        window.alert('Erro. Verifique os dados e tente novamente novamente!')
    } else {
        window.alert('Tudo ok!')
    }
}