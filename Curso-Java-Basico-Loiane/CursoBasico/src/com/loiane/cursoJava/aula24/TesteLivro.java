package com.loiane.cursoJava.aula24;

import java.util.Date;

public class TesteLivro {

	public static void main(String[] args) {
		LivroDeBiblioteca livro = new LivroDeBiblioteca();
		
		livro.anoLancamento = 2023;
		livro.autor = "Loiane";
		livro.emprestado = true;
		livro.dataEntrega = new Date(); // Dando a data normal
		
	}

}
