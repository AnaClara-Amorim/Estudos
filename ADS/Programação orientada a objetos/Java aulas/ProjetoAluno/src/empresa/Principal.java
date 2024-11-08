package empresa;

public class Principal {

	public static void main(String[] args) {
		
		Aluno a1 = new Aluno("Mario", 111, 0.1, new Curso("Engenharia", 1000));
		
		a1.info();
		
		//System.out.println("Pagamento: " + a1.pagamento());
		
		
	}

}
