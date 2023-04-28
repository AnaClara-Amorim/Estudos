let num = [5, 8, 2, 9, 3] // Vetor criado

console.log(`Nosso vetor é o ${num}`) // Mostrando o vetor

num[5] = 6 // Adicionando o valor 6 na posição de índice 5, lembrando que o índice começa em zero

console.log(num) // Mostrando o vator com o novo elemento

num.push(7) // Este comando adiciona o elemento no final do vetor 

console.log(num) 

console.log (`O vetor tem ${num.length} posições`) //Mostra quantos elementos tem
num.sort() // Coloca os valores em ordem crescente
console.log (`O primeiro valor do vetor é ${num[0]}`) // Mostra o valor no índice 

// PARA MOSTRAR O VETOR SEM A FORMATAÇÃO PADRÃO

for (let pos = 0; pos <num.length; pos++){ 
    console.log(`A posição ${pos} tem valor ${num[pos]}`)
}

// JEITO MAIS SIMPLIFICADO, otimizado para arrays

for (let pos in num) { //Para cada posição em num
    console.log (num[pos])
}

