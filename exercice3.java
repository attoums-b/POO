import java.util.Scanner;
public class exercice3 {
    public static double convertirCelciusEnFarenheit(double t){
        double convfarenheit = (t * 1.8) + 32;
        return convfarenheit;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("entrez la valeur de la temperature(en dégres celcius): ");
        double t = scanner.nextInt();

        double farenheit = convertirCelciusEnFarenheit(t);
        System.out.println("la température en farenheit:  "+ farenheit + "F");

        scanner.close();


    }

}
