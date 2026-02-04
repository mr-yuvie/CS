#include <stdio.h>

// 1. Write a program to find divisor or factorial of a given number.
// 1.1 a. Write an algorithm to find sum of two numbers.
// b. Write an algorithm that reads two numbers and print the value of the largest number.

int Practical_1() {
    int num, i, choice;
    printf("Enter number: ");
    scanf("%d", &num);

    printf("Enter choice[1: Divisor, 2: Factorial]: ");
    scanf("%d", &choice);

    if (choice == 1) {
        if (num < 0) {
            num = num - (2 * num);
            for (i = num; i > 0; i--) {
                if (num % i == 0) {
                    printf("%d\n", i);
                }
            }
        } else {
            for (i = num; i > 0; i--) {
                if (num % i == 0) {
                    printf("%d\n", i);
                }
            }
            return 0;
        }
    }

    else if (choice == 2) {
        int factorial = 1;
        if (num < 0) {
            printf("Negative number entered.");
            return 0;
        } else {
            for (i = num; i > 0; i--) {
                factorial *= i;
            }
            printf("Factorial: %d", factorial);
            return 0;
        }
    }

    else {
        printf("Wrong choice entered. Try again.");
        return 0;
    }
}

int Practical_1_1() {
    int num1, num2, sum;
    printf("Enter first number: ");
    scanf("%d", &num1);
    printf("Enter Second Number: ");
    scanf("%d", &num2);
    sum = num1 + num2;
    printf("Sum: %d", sum);
}

int Practical_1_2() {
    int num1, num2;
    printf("Enter first number: ");
    scanf("%d", &num1);
    printf("Enter Second Number: ");
    scanf("%d", &num2);
    printf("Largest number: %d", num1 > num2 ? num1 : num2);
}

void Practical_1_A() {
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    int rev = 0;
    while (n != 0) {
        rev = rev * 10 + (n % 10);
        n = n / 10;
    }
    printf("Num: %d", rev);
}

void Practical_1_B() {
    int n, original;
    printf("Enter the number: ");
    scanf("%d", &n);
    original = n;
    int rev = 0;
    while (n != 0) {
        rev = rev * 10 + (n % 10);
        n = n / 10;
    }
    if (original == rev) {
        printf("Palindrome.");
    } else {
        printf("Not Palindrome.");
    }
}

void Practical_1_C() {
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    for (int i = 1; i <= 10; i++) {
        printf("%d\n", n * i);
    }
}

void Practical_1_D() {
    int num;
    int prime = 1;
    printf("Enter number: ");
    scanf("%d", &num);
    for (int i = 2; i < num; i++) {
        if (num % i == 0) {
            prime = 0;
            printf("Not Prime.");
            break;
        }
    }
    if (prime == 1) {
        printf("Prime.");
    }
}

void Practical_1_E() {
    int n;
    printf("Enter number of terms: ");
    scanf("%d", &n);
    int a = 0, b = 1;
    int c;
    printf("%d\n", a);
    printf("%d\n", b);
    for (int i = 0; i < n; i++) {
        c = a + b;
        a = b;
        b = c;
        printf("%d\n", c);
    }
}

int main() {
    // Practical_1();
    // Practical_1_1();
    // Practical_1_2();
    // Practical_1_A();
    // Practical_1_B();
    // Practical_1_C();
    // Practical_1_D();
    // Practical_1_E();
}
