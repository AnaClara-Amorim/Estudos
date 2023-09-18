package com.loiane.cursoJava.aula29;

public class Carro {
	// Atributos
			String marca;
			String modelo;
			int numPassageiros;
			double capCombustivel;
			double consumoCombustivel;
			
			// Inicializando construtor 
			Carro (){
				System.out.println("Classe carro foi instanciada");
				consumoCombustivel = 11;
		}
			
			// Inicialiazndo a classe com todos os parametros
			
			Carro (String marca_, String modelo_, int numPassageiros_, double capCombustivel_, double consumoCombustivel_) {
				marca = marca_;
				modelo = modelo_;
				numPassageiros = numPassageiros_;
				capCombustivel = capCombustivel_;
				consumoCombustivel = consumoCombustivel_;
			}
}
