import java.util.Random;
import java.util.Scanner;

public class exercice5 {


    public static int genererNombreAleatoire(int min, int max){
        Random rand = new Random();
        int nombreAleatoire = rand.nextInt(max-min) + min;
        return nombreAleatoire;


    }
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        System.out.print("entrez le min : ");
        int min = scanner.nextInt();
        System.out.print("entrez le max: ");
        int max = scanner.nextInt();

        int nbAl = genererNombreAleatoire(min,max);
        System.out.println(nbAl);

        scanner.close();

    }


}
