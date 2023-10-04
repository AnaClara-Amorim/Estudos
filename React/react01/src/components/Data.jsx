export default function Data(){

    let nome = "Ana"; // Inserindo a variável abaixo
    let cliente = {
        nome: "Cliente1",
        email: "cliente@mail.com"
    }

    function add (a,b) {
        return a + b 
    }

    return(
        <>
            <p>Nome: {nome}</p>
            <p>Nome do cliente: {cliente.nome}</p>
            <p>Email do cliente: {cliente.email}</p>
            <p>A soma de 100 + 200 é igual = {add (100, 200)}</p>
        </>
    )
}