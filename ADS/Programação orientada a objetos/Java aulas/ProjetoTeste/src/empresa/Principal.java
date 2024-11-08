package empresa;

import java.util.ArrayList;
import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		System.out.println("Alô, mamãe!");
		Scanner teclado = new Scanner(System.in);
		
		//Aluno a = new Aluno(); // Instânciando objeto
		
		// Acessando objetos
		
		//a.cpf = "12345";
		//a.nome = "Super Mario";
		//a.matricula = 1111;
		
		//System.out.println("Matrícula: " + a.matricula);
		//System.out.println("Nome: " + a.nome);
		//System.out.println("Cpf: " + a.cpf);
				
		// Depois de criado um método no Aluno
		
		//a.info();
		
		//Aluno b = new Aluno();
		
		//b.cpf = "2345";
		//b.matricula = 22222;
		//b.nome = "Yoshi";
		
		//b.info();
		
		Carro c = new Carro();
		
		
		System.out.println(Carro.milhasParaMetros(10));
		
		
		Turma nova = new Turma();
		
		nova.prof = new Professor();
		nova.prof.nome = "Leonardo"; 
		nova.alunos = new ArrayList();
		nova.alunos.get(0).nome = "Super Mario";
		
		//a.cpf = "123.123.123-3";
		//a.nome = "Super";
		//a.matricula = 11101;
		
		Aluno d = new Aluno (1111, "Nome", "123.123.123"); //Passado por construtor
		d.info();
		
		
	}

}
