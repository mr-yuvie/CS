#include <math.h>
#include <stdio.h>
#include <string.h>

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

int sum_n_numbers_recursion(int n) {
    if (n == 1) {
        return 1;
    }
    int sum = n + sum_n_numbers_recursion(n - 1);
    return sum;
}

void fibonacci_sequence() {
    int n;
    printf("Enter number: ");
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

void avg_3_nums_array() {
    int marks[3];
    printf("Enter marks of Physics: ");
    scanf("%d", &marks[0]);
    printf("Enter marks of Chemistry: ");
    scanf("%d", &marks[1]);
    printf("Enter marks of Maths: ");
    scanf("%d", &marks[2]);
    printf("Percentage is: %d%%", (marks[0] + marks[1] + marks[2]) / 3);
}

void count_odd() {
    int len;
    printf("Enter length of Array: ");
    scanf("%d", &len);
    int arr[len];
    for (int i = 0; i < len; i++) {
        printf("Enter num: ");
        scanf("%d", &arr[i]);
    }
    int counter = 0;
    for (int i = 0; i < len; i++) {
        if (arr[i] % 2 == 1) {
            counter++;
        }
    }
    printf("Total Odd numbers: %d", counter);
}

void Reverse_Array() {
    int len;
    printf("Enter length of Array: ");
    scanf("%d", &len);
    int arr[len];
    for (int i = 0; i < len; i++) {
        printf("Enter num: ");
        scanf("%d", &arr[i]);
    }
    for (int i = 0; i < len / 2; i++) {
        int a = arr[i];
        int b = arr[len - i - 1];
        arr[i] = b;
        arr[len - i - 1] = a;
    }
    for (int i = 0; i < len; i++) {
        printf("%d\n", arr[i]);
    }
}

void table_n_array() {
    int n;
    printf("Enter total tables: ");
    scanf("%d", &n);
    int arr[n][10];
    for (int i = 0; i < n; i++) {
        printf("Enter number: ");
        scanf("%d", &arr[i][0]);
        for (int j = 2; j < 11; j++) {
            arr[i][j - 1] = arr[i][0] * j;
        }
    }
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d x %d = %d\t", j + 1, i + 1, arr[j][i]);
        }
        printf("\n");
    }
}

void largest_num_array() {
    int arr[] = {10, 20, 60, 45, 789, 47};
    int temp = 0;
    for (int i = 0; i < 6; i++) {
        if (temp < arr[i]) {
            temp = arr[i];
        }
    }
    printf("%d", temp);
}

void string_length() {
    char name[20];
    printf("Enter name: ");
    fgets(name, 20, stdin);
    int length = 0;
    for (int i = 0; name[i] != '\0'; i++) {
        length++;
    }
    printf("length: %d", length - 1);  // Because \0 is also included in the count
}

void string_input_using_characters() {
    char str[100];
    char ch;
    int i = 0;
    printf("Enter String: ");
    while (ch != '\n') {
        scanf("%c", &ch);
        str[i] = ch;
        i++;
    }
    str[i] = '\0';
    puts(str);
}

void string_slicing() {
    char str[100];
    printf("Enter String: ");
    fgets(str, 100, stdin);
    int n;
    int m;
    printf("Enter lower index: ");
    scanf("%d", &n);
    printf("Enter upper index: ");
    scanf("%d", &m);
    for (n; n < m + 1; n++) {
        printf("%c", str[n]);
    }
}

void vowels() {
    char str[100];
    printf("Enter String: ");
    fgets(str, 100, stdin);
    int count = 0;
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u') {
            count++;
        }
    }
    printf("Total Vowels: %d", count);
}

void lowercase_to_uppercase() {
    char str[100];
    printf("Enter String: ");
    fgets(str, 100, stdin);
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] > 96 && str[i] < 123) {
            printf("%c", str[i] - 32);
        } else {
            printf("%c", str[i]);
        }
    }
}

void structure_address() {
    typedef struct address {
        int house_num;
        int block;
        char city[30];
        char state[30];
    } add;
    int total_people;
    printf("Enter total people: ");
    scanf("%d", &total_people);
    add adds[total_people];
    for (int i = 0; i < total_people; i++) {
        printf("Enter info of person %d: \n", i + 1);
        scanf("%d", &adds[i].house_num);
        scanf("%d", &adds[i].block);
        scanf("%s", &adds[i].city);
        scanf("%s", &adds[i].state);
    }
    for (int i = 0; i < total_people; i++) {
        printf("Info of person %d: ", i + 1);
        printf("%d\t", adds[i].house_num);
        printf("%d\t", adds[i].block);
        printf("%s\t", adds[i].city);
        printf("%s\t", adds[i].state);
        printf("\n");
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
    // prime_numbers_in_range();
    // printf("Sum is: %d", sum_n_numbers_recursion(3));
    // fibonacci_sequence();
    // avg_3_nums_array();
    // count_odd();
    // Reverse_Array();
    // table_n_array();
    // largest_num_array();
    // string_length();
    // string_input_using_characters();
    // string_slicing();
    // vowels();
    // lowercase_to_uppercase();
    // structure_address();
    return 0;
}