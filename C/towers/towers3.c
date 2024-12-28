#include <stdio.h>

// https://www.reddit.com/r/learnpython/comments/18ctg93/i_cannot_understand_how_the_towers_of_hanoi/


// to solve this think about the calls on the stack
// 

// Recursive function to solve Tower of Hanoi
void solve_tower(int disk_count, char source_rod, char target_rod, char auxiliary_rod) {
    // Display the current function call for debugging
    printf("solve_tower called with disk_count = %d, source_rod = %c, target_rod = %c, auxiliary_rod = %c\n",
           disk_count, source_rod, target_rod, auxiliary_rod);

    // Base case: If there is only one disk, move it directly to the target rod
    if (disk_count == 1) {
        printf("Move disk 1 from %c to %c\n", source_rod, target_rod);
        return; // End this branch of recursion
    }

    // Step 1: Move the top (disk_count - 1) disks to the auxiliary rod
    printf("Step 1: Move top %d disks from %c to %c using %c as auxiliary\n",
           disk_count - 1, source_rod, auxiliary_rod, target_rod);
    solve_tower(disk_count - 1, source_rod, auxiliary_rod, target_rod);

    // Step 2: Move the largest disk directly to the target rod
    printf("Step 2: Move disk %d from %c to %c\n", disk_count, source_rod, target_rod);
    printf("Move disk %d from %c to %c\n", disk_count, source_rod, target_rod);

    // Step 3: Move the (disk_count - 1) disks from the auxiliary rod to the target rod
    printf("Step 3: Move top %d disks from %c to %c using %c as auxiliary\n",
           disk_count - 1, auxiliary_rod, target_rod, source_rod);
    solve_tower(disk_count - 1, auxiliary_rod, target_rod, source_rod);
}

int main() {
    int disk_count = 8; // Number of disks in the Tower of Hanoi puzzle
    printf("Solving Tower of Hanoi for %d disks:\n", disk_count);

    // Initial call to solve the puzzle
    solve_tower(disk_count, 'A', 'C', 'B'); // 'A' is source, 'C' is target, 'B' is auxiliary

    return 0;
}
