import java.util.Arrays;
import java.util.Scanner;

class ValidPermutations {

    static int findValidPermutaions(int arr[]) {
        Arrays.sort(arr);
        int opreations = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] <  i + 1) {
                opreations += i + 1 - arr[i];
                arr[i] = i + 1;
            }
        }
        return opreations;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int number = sc.nextInt();
            int arr[] = new int[number];

            for (int i = 0; i < number; i++) {
                arr[i] = sc.nextInt();
            }

            System.out.println(findValidPermutaions(arr));
        }
    }
}
