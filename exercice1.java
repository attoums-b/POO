import java.util.Scanner;

public class exercice1 {
    public static int somme(int a , int b){
        return a + b;

    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("entrez la valeur de a: ");
        int a = scanner.nextInt();
        System.out.print("entrez la valeur de b: ");
        int b = scanner.nextInt();
        int resultat = somme(a,b);
        System.out.println("la somme de "+ a + " et " + b + " donne: "+ resultat);

        scanner.close();

    }




}
