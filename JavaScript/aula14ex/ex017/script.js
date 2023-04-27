function tabuada() {
    let num = document.getElementById('txtn')
    let tab = document.getElementById('seltab')

    if (num.value.length == 0) {
        window.alert('Por favor, digite um número!')
    } else {
        let n = Number(num.value)
        let c = 1
        tab.innerHTML = '' //Para limpar a tabuada
        while (c <=10 ) {
            let item = document.createElement('option') //Foi criado aqui e não no html
            item.text = `${n} x ${c} = ${n*c}`
            item.value = `tab${c}`//Linha para dar valor, faz sentido em outra linguagens
            tab.appendChild(item)
            c++
        }
    }
}