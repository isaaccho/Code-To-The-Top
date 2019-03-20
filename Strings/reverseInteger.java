public class reverseInteger {
    public static void main(String[] args) {
        int num = 4529678;
        int result = 0;
        while (num != 0) {
            result = result * 10 + (num % 10);
            num = num / 10;
        }
        System.out.println("The reversed integer is:");
        System.out.println(result);

    }
}