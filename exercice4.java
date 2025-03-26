import java.util.Scanner;

public class exercice4 {
    public static boolean verifierSiPremier(int n){
        int nbdiv = 0;
        for(int i = 1; i <= n; i++){
            if(n %i == 0){
                nbdiv += 1;
            }
        }
        return nbdiv == 2;

    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("entrez la valeur à vérifier : ");
        int n = scanner.nextInt();

        boolean res = verifierSiPremier(n);
        System.out.println(res);

        scanner.close();

    }

}
