package com.loiane.cursoJava.aula19;

public class Arrays {

	public static void main(String[] args) {
		// Armazenar temperatura do ano todos dias
				
		double [] temperaturas = new double [365];
		
		temperaturas [0] = 31.3;
		
		System.out.print("O tamanho do array é: " + temperaturas.length);
		
		for (int i =0; i < temperaturas.length; i++) {
			System.out.println("O valor da temperatura do dia " + (i+1) + " é: " + temperaturas[i]);
		}
		
		//For melhorado
		
		for (double temp : temperaturas) {
			System.out.println(temp);
		}
		
	}

}
