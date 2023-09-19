package com.loiane.cursoJava.aula31;

// Retirando o class, só vai ser visível dentro do pacote da aula 31
 class Carro {

	public String marca;
	String modelo;
	int numPassageiros;
	double capCombustivel;
	private double consumoCombustivel; // Com o private só deixa visivel dentro da propria classe
	
	public void exibirAutonomia() {
		System.out.println("A autonomia do carro é: " + this.capCombustivel * this.consumoCombustivel + " km");
	}

	public double obterAutonomia() {

		System.out.println("Método obterAutonomia foi chamado.");

		return this.capCombustivel * this.consumoCombustivel;
	}

	double calcularCombustivel(double km) {

		double qtdCombustivel = km / this.consumoCombustivel;

		return qtdCombustivel;
	}
}
