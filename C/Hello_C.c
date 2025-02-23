#include <math.h>
#include <stdio.h>  // Preprocessor director

int Hello_C() {
    printf("Hello\n");
    printf("World\n");
    int number = 25;
    char hashtag = '#';
    int age = 22;
    age = 24;
    float pi = 3.14;
    printf("age is %d\n", age);          // %d: int
    printf("pi is %f\n", pi);            // %f: float
    printf("hashtag is %c\n", hashtag);  // %c: char
    // for input: scanf
    printf("Enter age: ");
    scanf("%d", &age);
    printf("age is: %d\n", age);
    return 0;
}

/* Data types- char/signed car, unsigned char, int/signed int, unsigned int,
 short int/unsigned short int, signed short int, long int/signed log int,
 unsigned long int, float, double, long double */

// Integer Constants, Real Constants (2.0,3.14,-2.4), Character Constants

int type_declaration() {
    int a = 22;
    int b = a;
    int c = b + 6;
    int d = 1;
    int x, y, z;
    x = y = z = 20;
    int j = 3, k = 2;
    printf("%f\n", pow(j, k));  // 9.0000
    printf("%d\n", c % b);
    printf("%d\n", 4 / 2);
    printf("%d", (int)1.9999);  // Foreful tyoe casting
    return 0;
}

// printf("%d%d", a, b, c, d, x, y, z, j, k);

// Control Instructions => Sequence Control, Decision Control, Loop Control,
// Case Control Logical Operators => &&, ||, ! Operator Precedence => !, Bodmas,
// relational operators, logical operators, assignment operator Shorthand
// notations also work like +=, -= etc.

int logical_operators() {
    printf("%d\n", (3 > 4) || (4 > 3));
    printf("%d\n", (200 > 1) && (3 >= 3));
    printf("%d\n", !(3 > 4) && !(2 > 4));
    return 0;
}

int conditional_operators_1() {
    int age;
    printf("Enter age: ");
    scanf("%d", &age);

    if (age >= 18 && age < 60) {
        printf("Adult\n");
    } else if (age > 60) {
        printf("Senior Citizen");
    } else {
        printf("Not an Adult\n");
    }
    // Ternary Operator can also be used ==> condition ? true : false;
    return 0;
}

void conditional_operators_2() {
    int marks;
    printf("Enter Marks: ");
    scanf("%d", &marks);
    switch (marks) {
        case 100:
            printf("A+\n");
            break;

        default:
            printf("Not A+, Skill Issue.\n");
            break;
    }
}

void Loop_Control() {
    int x = 0;
    for (x; x < 10; x++) {  // x++(post increment operator) => Use then Increase,
                            // ++x(pre increment operator) => Increase then Use
        printf("Hello World\n");
    }
    while (x < 10) {
        printf("Hello World\n");
        x += 1;
    }
    do {
        printf("%d\n", x);
        x++;
    } while (x <= 10);
}

int main() {
    // Hello_C();
    // type_declaration();
    // logical_operators();
    // conditional_operators_1();
    // conditional_operators_2();
    Loop_Control();
}