#include <stdio.h>

int count_down(int x){
    printf("x on entry to function = %d\n", x);
    if(x == 0){
        printf("Base case hit here\n");
    return 0;
    }
    else{
        printf("Recursive call 1st branch: x - 1 = %d\n", x - 1);
        count_down(x - 1);
        printf("Recursive call 2nd branch: x - 1 = %d\n", x - 1);
        count_down(x - 1);
    };
}

int main(void){

int iterations = 3;

count_down(iterations);

}