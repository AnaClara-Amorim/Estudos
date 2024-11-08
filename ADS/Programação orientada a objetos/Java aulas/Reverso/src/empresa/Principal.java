package empresa;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {

		// Array 
		
		ArrayList<Integer> megaSena = new ArrayList<Integer>();
		
		// Variáveis primitivas: int, float, double, char
		// Classes: String, Integer
		Scanner teclado = new Scanner (System.in);
		
		ArrayList<String> listaNomes = new ArrayList<String>();
		
		System.out.println("Digite a quantidade de nomes: ");
		int qtd = teclado.nextInt();
		
		String nome;
		for (int i = 0; i < qtd; i++) {
			nome = teclado.next();
			listaNomes.add(nome);
		}
		
		for (int i = qtd -1; i >=0; i--) {
			System.out.println(listaNomes.get(i));
		}
		
		// Ou
		
		System.out.println("Ordem normal");
		System.out.println(listaNomes);
		
		Collections.reverse(listaNomes);
		
		System.out.println("Ordem reversa");
		System.out.println(listaNomes);
	
	}
}
