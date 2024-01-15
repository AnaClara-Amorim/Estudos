package br.com.dfcodelab7.introducao.classes;

public class Pessoa {
	
	public String nome;
	public int idade;
	public String email;	
	
	// Ctrl + espaço cria construtor
 	public Pessoa(){
 		
 		
 	}

	@Override
	public String toString() {
		return "Pessoa [nome=" + nome + ", idade=" + idade + ", email=" + email + "]";
	}
 
 
 

}