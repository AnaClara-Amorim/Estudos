package com.loiane.cursoJava.aula26;

class Carro {
	// Atributos
	String marca;
	String modelo;
	int numPassageiros;
	double capCombustivel;
	double consumoCombustivel;
	
	double obterAutonomia() {
		
		System.out.println("Metodo obterAutonomia foi chamado");
		
		return capCombustivel * consumoCombustivel;
		}
}
