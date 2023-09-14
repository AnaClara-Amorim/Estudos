package com.loiane.cursoJava.aula25;

public class Carro {
	
	// Atributos
	String marca;
	String modelo;
	int numPassageiros;
	double capCombustivel;
	double consumoCombustivel;
	
	// Métodos
	void exibirAutonomia(){
		System.out.println("A autonomia do carro é: " + capCombustivel * consumoCombustivel + "km");
	}
	
	
	
}

