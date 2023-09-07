package com.loiane.cursoJava.aula15;

import java.util.Scanner;

public class WhileDoWhile {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner (System.in);
		int numero;
		do {
            System.out.print("Digite um número positivo: ");
           numero = scanner.nextInt();
        } while (numero <= 0);
		
		while (numero >= 1) {
            System.out.println(numero);
            numero--;
        }

	}

}
