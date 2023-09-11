package exercicios;

import java.util.Scanner;

public class Ex01 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner (System.in);
		
		int [] vetorA = new int[5];
		int [] vetorB = new int [vetorA.length];
		
		for (int i = 0; i < vetorA.length; i++) {
			System.out.println("Entre com o valor da posição " + i);
			
			vetorA [i] = scan.nextInt();
			vetorB [i] = vetorA[i];			
		}
		
				
		/*for (int i = 0; i < vetorA.length; i++) {
			vetorB [i] = vetorA[i];
		} */
		System.out.println ("Vetor A = ");
		for (int i = 0; i < vetorA.length; i++) {
			System.out.println(vetorA[i]);
		}
		
		System.out.println ("Vetor B = ");
		for (int i = 0; i < vetorA.length; i++) {
			System.out.println(vetorB[i]);
		}
		
		

	}

}
