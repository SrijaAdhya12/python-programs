import java.util.Scanner;

public class LuckyNumber {

    public static int FindLuckyNumber(String word) {
        int summation = 0;
        for (int i = 0; i < word.length(); i++) {
            int ascval = (int) word.charAt(i);
            if (ascval % 2 != 0 || i+1 % 2 != 0) {
                summation += (ascval * (i+1));
            }
        }
        return summation;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            String word = sc.nextLine();
            int luckyNumber = FindLuckyNumber(word);
            System.out.println(luckyNumber);
        }
    }
}
