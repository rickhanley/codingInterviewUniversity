#include <stdio.h>

void move_tower(int n, char source, char target, char auxiliary) {
    // printf("Function called with int n = %d   source: %c     target: %c     aux: %c\n", n, source, target, auxiliary);
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", source, target);
        return;
    }

    move_tower(n - 1, source, auxiliary, target);
    printf("Move disk %d from %c to %c\n", n, source, target);
    move_tower(n - 1, auxiliary, target, source);
}

int main() {
    int n = 3; // Number of disks
    move_tower(n, 'A', 'C', 'B');  // A, B and C are names of rods
    
    return 0;
}