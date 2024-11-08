package empresa;

public class Principal {

	public static void main(String[] args) {
		
		Nota mario = new Nota();
		
		Nota luigi = new Nota(9,8,3);
		System.out.println("Média Luigi");
		luigi.resultado();
		System.out.println();
		
		mario.setNota1 (9);
		mario.setNota2 (10);
		
		mario.setFaltas(5);

		mario.resultado();
		
		mario.setNota1(2);
		mario.setFaltas(10);
		
		mario.resultado();
		
	}

}
