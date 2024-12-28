#include <stdio.h>

void solve_tower(int disk_count, char source, char target, char auxiliary, int depth) {
    // Print the depth to show the tree structure
    for (int i = 0; i < depth; i++) {
        printf("  ");
    }
    printf("solve_tower(disk_count=%d, source=%c, target=%c, auxiliary=%c)\n",
           disk_count, source, target, auxiliary);

    // Base case
    if (disk_count == 1) {
        for (int i = 0; i < depth; i++) {
            printf("  ");
        }
        printf("Move disk 1 from %c to %c\n", source, target);
        return;
    }

    // Recursive calls
    solve_tower(disk_count - 1, source, auxiliary, target, depth + 1);
    for (int i = 0; i < depth; i++) {
        printf("  ");
    }
    printf("Move disk %d from %c to %c\n", disk_count, source, target);
    solve_tower(disk_count - 1, auxiliary, target, source, depth + 1);
}

int main() {
    int n = 3; // Number of disks
    solve_tower(n, 'A', 'C', 'B', 0); // Pass initial depth as 0
    return 0;
}
