package com.loiane.cursoJava.aula24;

public class TesteLampada {

	public static void main(String[] args) {

		Lampada lampada = new Lampada();
		lampada.modelo = "A60";
		lampada.tensao = "Bivolt";
		lampada.garantiaMeses = 36;
		
		lampada.tipos = new String[5]; // Criação do array para seu uso
		lampada.tipos[0] = "Abajour";
		
	}

}
