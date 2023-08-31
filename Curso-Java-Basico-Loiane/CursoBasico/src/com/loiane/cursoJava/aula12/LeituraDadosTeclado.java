package com.loiane.cursoJava.aula12;
import java.util.Scanner;

public class LeituraDadosTeclado {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		// Lendo uma linha inteira
		
		System.out.println("Digite seu nome: ");
		String nomeCompleto = scan.nextLine();
		System.out.println("Seu nome é: " + nomeCompleto);
		
		// Lendo um tipo de dado específico
		
		/* System.out.println("Digite seu primeiro nome: ");
		String primeiroNome = scan.next();
		System.out.println("Seu primeiro nome é: " + primeiroNome); // Aqui só vai pegar o primeiro nome 
		
		System.out.println("Digite sua idade: ");
		int idade = scan.nextInt();
		System.out.println("Sua idade é: " + idade);		
		
		System.out.println("Digite sua altura: ");
		double altura = scan.nextDouble();
		System.out.println("Sua altura é: " + altura); */
		
		System.out.println("Digite o seu primeiro nome, idade, quantidade de filhos, altura e se tem bichinhos de estimação: ");
		String primeiroNome = scan.next();
		int idade = scan.nextInt();
		byte qtdFilhos = scan.nextByte();
		float altura = scan.nextFloat();
		boolean temPet = scan.nextBoolean();
		
		System.out.println("Você digitou os seguintes valores: ");
		System.out.println(primeiroNome);
		System.out.println(idade);
		System.out.println(qtdFilhos);
		System.out.println(altura);
		System.out.println(temPet);
		
		
		
		
		

	}

}
