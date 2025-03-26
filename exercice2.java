import java.util.Scanner;

public class exercice2 {
    // calcul de la factorielle

    public static int factorielle(int nbr){
        if (nbr < 0){
            System.out.println("pas de factorielle d'un nombre négatif!!");
        }
        int fact = 1;
        for (int i = 1 ; i <= nbr; i++){
            fact *= i;
        }
        return fact;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("entrez la valeur de nbr: ");
        int nbr = scanner.nextInt();

        int f = factorielle(nbr);
        System.out.println("la factorielle de "+ nbr + " donne: "+ f);

        scanner.close();

    }

}



