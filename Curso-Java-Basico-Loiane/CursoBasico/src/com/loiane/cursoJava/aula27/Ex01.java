package com.loiane.cursoJava.aula27;

public class Ex01 {

	public static void main(String[] args) {
		
		Lampada lampada = new Lampada();
		
		lampada.ligar();
		
		if (lampada.ligada) {
		System.out.println("A lâmpada está ligada: " + lampada.ligada);
		} else {
			System.out.println("A lâmpada está desligada");
		}
		
		lampada.desligar();
		
		if (lampada.ligada) {
			System.out.println("A lâmpada está ligada: " + lampada.ligada);
			} else {
				System.out.println("A lâmpada está desligada");
			}
		
		lampada.mostrarEstado(); // Forma de organizar o código
		
		lampada.mudarEstado();
		
		lampada.mostrarEstado(); 
	}

}
