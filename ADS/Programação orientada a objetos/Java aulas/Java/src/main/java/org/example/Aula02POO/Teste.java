package org.example.Aula02POO;

public class Teste {
    public static void main(String[] args) {

        // Instanciando/criando o objeto
        Calculadora calculus = new Calculadora();


        // Chamando métodos
        System.out.println(calculus.soma(1,2));
        System.out.println(calculus.subtracao(1,2));
        System.out.println(calculus.mutiplicacao(1,2));
        System.out.println(calculus.divisao(1,2));
    }
}
