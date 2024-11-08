package empresa;

public class Principal {

	public static void main(String[] args) {

		Conta c1 = new Conta(1111, "Mario", 2000, 5000);
		
		c1.info();
		
		c1.sacar(200);
		
		System.out.println();
		c1.info();
		
		c1.depositar(500);


		System.out.println();
		
		c1.info();
	}

}
