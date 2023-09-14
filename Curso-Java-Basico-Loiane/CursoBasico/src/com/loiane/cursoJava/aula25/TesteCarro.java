package com.loiane.cursoJava.aula25;

public class TesteCarro {

	public static void main(String[] args) {

		Carro van = new Carro();
		
		van.marca = "Fiat";
		van.modelo = "Ducato";
		van.numPassageiros = 10;
		van.capCombustivel = 100;
		van.consumoCombustivel = 0.2;
		
		//Output
		System.out.println(van.marca);
		System.out.println(van.modelo);
		
		//Chamando método simples
		van.exibirAutonomia();

	}

}
