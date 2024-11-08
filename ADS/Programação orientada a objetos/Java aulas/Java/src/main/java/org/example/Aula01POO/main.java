package org.example.Aula01POO;

public class main {
    public static void main(String[] args) {

        // Criando objeto Sky

        // Nome da classe / Nome do objeto = novo Gato = Sky

        // Passando os parâmetro e preenchendo os atributos
        Gato sky = new Gato("Sky", "Preta e Branca", 3, 50);

        // Chamando método
        sky.miar();
        System.out.println(sky.miar2());
    }
}
