package exercicios;

import java.util.Scanner;

public class Ex06 {

	public static void main(String[] args) {
		Scanner scan = new Scanner (System.in);
		
		int [] vetorA = new int[10];
		int [] vetorB = new int [vetorA.length];
		int [] vetorC = new int [vetorA.length];
		
		for (int i = 0; i < vetorA.length; i++) {
			System.out.println("Entre com o valor do vetorA da posição " + i);
			vetorA [i] = scan.nextInt();		
		}
		
		for (int i = 0; i < vetorB.length; i++) {
			System.out.println("Entre com o valor do vetorB da posição " + i);
			vetorB [i] = scan.nextInt();		
			
		}
		
		for (int i = 0; i < vetorB.length; i++) {
			vetorC[i] = vetorA[i]+vetorB[i];
		}
		
		System.out.println ("Vetor A = ");
		for (int i = 0; i < vetorA.length; i++) {
			System.out.println(vetorA[i]);
		}
		
		System.out.println ("Vetor B = ");
		for (int i = 0; i < vetorA.length; i++) {
			System.out.println(vetorB[i]);
		}
		
		System.out.println ("Vetor C = ");
		for (int i = 0; i < vetorA.length; i++) {
			System.out.println(vetorC[i]);
		}
		
	}

}
