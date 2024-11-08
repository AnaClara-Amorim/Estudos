package org.example.Exercicio01;

public class Lampada {

    private boolean estado;

    // Construtores
    public Lampada(boolean estado) {
        this.estado = false;}
    public Lampada(){}

    // Método get
    public boolean isEstado() {
        return estado;
    }

    // Método set
    public void setEstado(boolean estado) {
        this.estado = estado;}


    public void estado(){
        if (isEstado() == true){
            System.out.println("A LÂMPADA TÁ LIGADA");
        }
        else {
            System.out.println("A LÂMPADA TÁ DESLIGADA");
        }
    }

    public void ligar(){
        if (this.estado == false) {
            setEstado(true);}

    }

    public void desligar(){
        if (this.estado == true){
            setEstado(false);

        }
    }

}
