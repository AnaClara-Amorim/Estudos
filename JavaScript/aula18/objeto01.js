let amigo = {
    nome: 'Ana',
    sexo: 'F',
    peso: 48,
    engordar(p=0){
        //Pode ir um código assim
        this.peso +=p
    }
}
//console.log(typeof amigo) Vai aparecer que é um objeto, pois em js, um array é um objeto, e um objeto é um objeto
//console.log(amigo)
//console.log(amigo.nome)
amigo.engordar(2)
console.log(`${amigo.nome} pesa ${amigo.peso} kg`)
