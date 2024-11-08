package org.example.Aula01POO;

public class Gato {

    // Atributos da classe
    private String nome;
    private String cor;
    private int idade;
    private double tamanho;

    // Médoto construtor da classe, ele vai ser usado, para instanciar o objeto
    public Gato(String nome, String cor, int idade, double tamanho) {
        this.nome = nome;
        this.cor = cor;
        this.idade = idade;
        this.tamanho = tamanho;
    }

    public Gato() {

    };

    // Metódo miau

    // Quando você retorna uma string, você tem que colocar dentro do system out

    public void miar(){
        System.out.println("Miau");
    }

    // Geralmente mais utilizado em estudo, para ver no console
    public String miar2(){
        return "Miau";
    }
}
