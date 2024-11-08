package empresa;

public class Carro {

	String nome;
	String modelo;
	float velocidade;
	static final double PI = 3.1415; // final indica que valor não pode ser modificado
	
	static float milhasParaMetros(float milhas) {
		return milhas*1600;
		
	}
}
