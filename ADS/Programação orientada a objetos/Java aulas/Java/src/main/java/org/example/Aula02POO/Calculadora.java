package org.example.Aula02POO;

public class Calculadora {

    // Atributos do objeto
    public double x;
    public double y;

    // Construtor da classe
    public Calculadora(double x, double y) {
        this.x = x;
        this.y = y;
    }

    // Construtor vazio vai ajudar a instanciar o objeto sem os atributos
    public Calculadora() {

    }

    // Criação dos métodos

    public double soma(double x, double y) { // Lembrar de tipar os parâmetro porque o java é fresco
        return x + y;
    }

    public double subtracao(double x, double y) {
        return  this.x - this.y; // This é para referênciar e ajudar a lembrar que o parâmetro vem dessa classe
    }

    public double mutiplicacao(double x, double y) {
        return x * y;
    }

    public double divisao(double x, double y) {
        return this.x / this.y; // portanto, vai dar nan, pq x - y não dá um resultado
    }

}
