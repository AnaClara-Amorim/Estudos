package com.loiane.cursoJava.aula27;

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

		double qtdCombustivel10 = van.calcularCombustivel(10);
		double qtdCombustivel15 = van.calcularCombustivel(15);
		
		System.out.println("qtdCombustivel10 = " + qtdCombustivel10);
		
		
	}

}
