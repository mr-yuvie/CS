#include <stdio.h>
#include <math.h>

void ToH(int n, char source, char auxiliary, char destination) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", source, destination);
        return;
    }

    ToH(n - 1, source, destination, auxiliary);
    printf("Move disk %d from %c to %c\n", n, source, destination);
    ToH(n - 1, auxiliary, source, destination);
}

int main() {
    int n;
    int total_steps;

    printf("Enter number of disks: ");
    scanf("%d", &n);

    ToH(n, 'S', 'A', 'D');
    total_steps = pow(2, n)-1;
    printf("Total steps: %d", total_steps);
    return 0;
}

// #include <stdio.h>

// void Practical_2_3(){
//     printf("Hello World\n");
// }

// int even_odd() {
//     int num;
//     printf("Enter num: ");
//     scanf("%d", &num);
//     if (num % 2 == 0) {
//         printf("Even");        
//     } else {
//         printf("Odd");
//     }
//     return 0;
// }

// int main(){
//     Practical_2_3();
//     even_odd();
// }
