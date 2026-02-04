#include <stdio.h>

// 2. Write a program to find sum of a geometric series
// 2.1 10% Discount is given, when a customer buys more than 100 items. Item cost will be entered by the user.
// Write an algorithm to calculate the final cost that has to be paid.

int Practical_2() {
    int first_term, common_ratio, no_of_terms, term, sum = 0;
    printf("Enter First Number: ");
    scanf("%d", &first_term);
    printf("Enter Common Ratio: ");
    scanf("%d", &common_ratio);
    printf("Enter Number of Terms: ");
    scanf("%d", &no_of_terms);
    term = first_term;
    for (int i = 0; i < no_of_terms; i++) {
        sum += term;
        term *= common_ratio;
    }
    printf("Sum of the Geometric Series: %d", sum);
}

int Practical_2_1() {
    int item_count;
    float item_cost, final_cost;
    printf("Enter Number of Items: ");
    scanf("%d", &item_count);
    printf("Enter Cost of the Item: ");
    scanf("%f", &item_cost);
    final_cost = item_count * item_cost;
    if (item_count > 100) {
        final_cost *= 0.9;
    }
    printf("Final cost: %f", final_cost);
}

int main() {
    // Practical_2();
    Practical_2_1();
}