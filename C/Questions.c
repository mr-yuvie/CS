#include <math.h>
#include <stdio.h>

int sum_two_nums() {
    int num_a, num_b;
    printf("Enter num a: ");
    scanf("%d", &num_a);
    printf("Enter num b: ");
    scanf("%d", &num_b);
    printf("Sum is: %d\n", num_a + num_b);
    return 0;
}

int area_square() {
    float side;
    printf("Enter side: ");
    scanf("%f", &side);
    printf("Area is: %f\n", side * side);
    return 0;
}

int area_circle() {
    float radius;
    printf("Enter radius: ");
    scanf("%f", &radius);
    printf("Area is: %f\n", 3.14 * radius * radius);
    return 0;
}

int divisible_by_2() {
    int a;
    printf("Enter a number: ");
    scanf("%d", &a);
    printf("%d\n", (a % 2) == 0);
    return 0;
}

int avg_3_nums() {
    int a = 3;
    int b = 4;
    int c = 5;
    printf("%d\n", (a + b + c) / 3);
    return 0;
}

void digit_or_not() {
    char a;
    printf("Enter a character: ");
    scanf("%c", &a);
    printf("%d\n", a <= '9' && a >= '0');
}

void smallest_num() {
    int a;
    int b;
    printf("Enter num 1: ");
    scanf("%d", &a);
    printf("Enter num 2: ");
    scanf("%d", &b);
    printf("Smallest num is: %d\n", (a < b) ? a : b);  // Ternary Operator
}

int even_odd() {
    int num;
    printf("Enter num: ");
    scanf("%d", &num);
    if (num >= 0) {
        printf("Positive number\n");
        if (num % 2 == 0) {
            printf("Even");
        } else {
            printf("Odd");
        }
    } else if (num < 0) {
        printf("Negative number\n");
    }
    return 0;
}

void uppercase_or_not() {
    char character_to_check;
    printf("Enter a letter: ");
    scanf("%c", &character_to_check);
    if (character_to_check >= 'A' && character_to_check <= 'Z') {
        printf("Uppercase\n");
    } else if (character_to_check >= 'a' && character_to_check <= 'z') {
        printf("Lowercase\n");
    } else {
        printf("Not a valid letter");
    }
}

void print_0_to_10() {
    for (int i = 0; i <= 10; i++) {
        printf("%d\n", i);
    }
}

int sum_n_numbers() {
    int n;
    int sum = 0;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    for (int i = 0; i <= n; i++) {
        sum += i;
    }
    printf("Sum is %d\n", sum);
    return 0;
}

void table_n() {
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    for (int i = 1; i <= 10; i++) {
        printf("%d\n", n * i);
    }
}

void cant_be_odd() {
    int num;
    do {
        printf("Enter num: ");
        scanf("%d", &num);
    } while (num % 2 == 0);
    printf("End.");
}

void print_odd() {
    for (int i = 5; i < 51; i += 2) {
        printf("%d\n", i);
    }
}

void factorial_of_n() {
    int num;
    int factorial = 1;
    printf("Enter num: ");
    scanf("%d", &num);
    for (int i = num; i > 0; i--) {
        factorial *= i;
    }
    printf("%d", factorial);
}

void prime_or_not() {
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

void prime_numbers_in_range() {
    int min_num;
    int max_num;
    printf("Enter min num: ");
    scanf("%d", &min_num);
    printf("Enter max num: ");
    scanf("%d", &max_num);
    for (int i = min_num; i < max_num; i++) {
        int prime = 1;
        for (int j = 2; j < i; j++) {
            if (i % j == 0) {
                prime = 0;
            }
        }
        if (prime == 1) {
            printf("%d\n", i);
        }
    }
}

int main() {
    // sum_two_nums();
    // area_square();
    // area_circle();
    // divisible_by_2();
    // avg_3_nums();
    // digit_or_not();
    // smallest_num();
    // even_odd();
    // uppercase_or_not();
    // print_0_to_10();
    // sum_n_numbers();
    // table_n();
    // cant_be_odd();
    // print_odd();
    // factorial_of_n();
    // prime_or_not();
    prime_numbers_in_range();
    return 0;
}

// bivarhoijoisdeolreoisdvj