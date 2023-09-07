package com.loiane.cursoJava.aula14;

import java.util.Scanner;

public class IfElse {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner (System.in);
		
		System.out.println("Entre com sua idade: ");
		
		int idade = scan.nextInt();
		
		if (idade >= 18) {
			System.out.print("Maior de idade");
		} else {
			System.out.print("Não é maior de idade");
		}

	}

}
