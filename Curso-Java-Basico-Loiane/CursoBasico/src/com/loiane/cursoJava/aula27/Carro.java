package com.loiane.cursoJava.aula27;

public class Carro {

	// Atributos
		String marca;
		String modelo;
		int numPassageiros;
		double capCombustivel;
		double consumoCombustivel;
		
		//Declaração de método com parâmetros
		double calcularCombustivel(double km) {
			double qtdCombustivel = km / consumoCombustivel;
			return qtdCombustivel;
		}
}
