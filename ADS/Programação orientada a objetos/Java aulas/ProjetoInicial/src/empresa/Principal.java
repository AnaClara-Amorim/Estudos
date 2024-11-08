package empresa;

import java.util.Scanner;


public class Principal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int idade = 10;
		String nome = "Ana";
		
		idade = idade + 2;
		
		double peso = 72.5;
		
		//float peso2 = 80.5f;
		
		Scanner teclado = new Scanner(System.in);
		System.out.println("Digite nome, idade e peso");
		nome = teclado.next(); // Pra ler string
		idade = teclado.nextInt();
		peso = teclado.nextDouble();
		
		
		
		System.out.println("Nome " + nome);
		System.out.printf("Idade é: %d\n", idade);
		System.out.printf("Peso é: %.2f\n", peso);
		
		if (idade < 18) {
			System.out.println("Acesso bloqueado!");
			
		}		
		else if  (idade < 65) {
			System.out.println("Adulto");
			
		}		
		else {
			System.out.println("Adulto idoso");
		}
		
		//int megaSena[] = {1, 2, 3, 4, 5};
		
		int numeros[] = new int [200];
		
		numeros[60] = 50;
		
	
	
	}

}
