var idade = 77
console.log(`Você tem ${idade} anos.`)
if (idade < 16) {
    console.log('Não vota.')
} else if (idade < 18 || idade > 65) {
        console.log('Voto opcional.')
} else { /* Aqui foi ocultado else if (idade >=18) */
    console.log ('Voto obritatório.')
}   

/* 
 FOI SIMPLIFICADO ACIMA POIS, É POSSÍVEL SIMPLIFICAR COM ELSE IF
var idade = 18

if (idade < 16) {
    console.log('Não vota')
} else {
    if (idade < 18){
        console.log('Voto opcional')
    } 
} */