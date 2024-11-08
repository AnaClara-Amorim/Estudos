package empresa;

public class Aluno {
	
	int matricula;
	String nome;
	String cpf;
	
	// Criando método
	
	void info() {
		System.out.println("Matrícula: " + matricula);
		System.out.println("Nome: " + nome);
		System.out.println("Cpf: " + cpf);
	}
	
	// Criando construtor
	
	Aluno (){
		System.out.println("Objeto foi criado");
	}
	
	Aluno (int pmatricula, String pnome, String pcpf){
		matricula = pmatricula;
		nome = pnome;
		cpf = pcpf;
	}
}
