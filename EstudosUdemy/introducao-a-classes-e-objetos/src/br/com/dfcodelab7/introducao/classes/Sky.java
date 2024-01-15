package br.com.dfcodelab7.introducao.classes;

public class Sky {
	
	public String especie;
	public int idade;
	public int peso;
	public String tutor;
	
	public Sky() {
		// TODO Auto-generated constructor stub
	}

	@Override
	public String toString() {
		return "Sky [especie=" + especie + ", idade=" + idade + ", peso=" + peso + ", tutor=" + tutor + "]";
	}
	
	public void miar() {
		System.out.println("MIAAAAAAAAAAAAAAAU!");
	}
	

}
