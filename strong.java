public class StrongNumbers {
    
    // Method to calculate factorial
    public static int factorial(int n) {
        int fact = 1;
        for (int i = 2; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }

    // Main method to find strong numbers between 1 to 5000
    public static void main(String[] args) {
        System.out.println("Strong numbers between 1 and 5000 are:");

        for (int num = 1; num <= 5000; num++) {
            int sum = 0, temp = num;

            while (temp > 0) {
                int digit = temp % 10;
                sum += factorial(digit);
                temp /= 10;
            }

            if (sum == num) {
                System.out.println(num);
            }
        }
    }
}

