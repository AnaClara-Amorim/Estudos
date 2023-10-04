import React from "react"

//Importando css

import './css/App.css'

//Components

import Buttom from "./buttom"
import Table from "./Table"
import Image from "./views/Image"
import Data from "./Data"
import Dados from "./Dados"

export /* default */ function App(){
    /* Aqui, pode haver lógiga de programação */
    return (
        <> {/* Pode-ser usar aqui apenas uma div */}
            <h1>Olá, Mundo!</h1>
           {/*  Utilizando classe em react é ClassName para não bater com o conceito de classe de javascript */}
            <h5 className="cor-texto">Outro texto</h5>
            <Buttom />
            <Table/>
            <Image / >
            <Data />
            <Dados/ >
        </>
    )
}


