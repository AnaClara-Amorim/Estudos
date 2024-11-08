package org.example.Aula04POO;
//  Encapsulamento: métodos getters e setters
public class Teste {
    public static void main(String[] args) {
        Carro van = new Carro();

        van.setMarca("Fiat");
        van.setModelo("Uno");
        van.setCapCombustivel(12);

        System.out.println(van.getMarca());
        System.out.println(van.getCapCombustivel());

    }
}
