import MeuComponente from "./components/MeuComponente" /* Foi criado no MeuComponente.jsx */

function App() {  

  return (
    <>
      <div>
        <h1>Olá, mundo!</h1>  
        <MeuComponente  />
        <MeuBotao conteudo='Primeiro clique'/>
        <MeuBotao conteudo= 'Segundo clique'/>
        <MeuBotao conteudo= 'Terceiro clique' />
      </div>    
      
    </>
  )
}

function MeuBotao(props) { /* foi passado um parametro props para alterar o conteudo do botão */
/* console.log(props.conteudo) */
  return (
    <button>{props.conteudo}</button>
  )
}



export default App
