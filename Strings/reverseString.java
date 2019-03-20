import java.util.Scanner;

public class reverseString {
    public static void main(String[] args) {
        // System.out.println("Please input a string");
        /// Scanner read = new Scanner(System.in);
        // String storeString = read.nextLine();
        String storeString = "testing";
        int len = storeString.length();
        String result = "";

        for (int i = len - 1; i >= 0; i--) {
            result = result + storeString.charAt(i);
        }
        System.out.println("The reversed string is:");
        System.out.println(result);
    }
}