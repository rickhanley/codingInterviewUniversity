#include <stdio.h>

int main(void) {
    for(long i = 0; i < 10000000; i++) {
        if(i % 381 == 0){
            printf("divisible by 381 %d times\n", (i / 381));
        }
    };
    printf("Done\n");
    return 0;
};

// i = 0

// while(i < 1000000):
//     if(i % 381 == 0):
//         print(f"divisible by 381 {(int) (i / 381)} times!")
//     i = i + 1
// print(f"Done!: {i}")