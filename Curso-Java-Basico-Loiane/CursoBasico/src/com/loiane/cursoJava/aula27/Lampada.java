package com.loiane.cursoJava.aula27;

public class Lampada {
	
	String modelo;
	String tensao;
	int potencia;
	String cor;
	String tipoLuz;
	int garantiaMeses;
	String [] tipos;
	boolean tipoAbajur;
	
	boolean ligada;
	
	void ligar () {
		ligada = true;
	}
	
	void desligar() {
		ligada = false;
	}
	
	// Métodos também podem ser usados para organizar o código
	void mostrarEstado() {
		if (ligada) {
			System.out.println("A lâmpada está ligada");
			} else {
				System.out.println("A lâmpada está desligada");
			}
	}
	
	void mudarEstado() {
		if (ligada) {
			desligar();
		} else {
			ligar();
		}
	}
		
}
