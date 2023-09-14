package com.loiane.cursoJava.aula26;

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
		
		// Chamando método com retorno
		
		van.obterAutonomia();
		
		double autonomia = van.obterAutonomia();
		
		System.out.println("A autonomia do carro é: " + autonomia);
		
		System.out.println("A autonomia do carro é: " + van.obterAutonomia());

	}

}
