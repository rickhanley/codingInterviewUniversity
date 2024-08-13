#include<stdio.h>

int main(void){
    double counter = 1;
    while(counter < 1000000000){
        // printf("%d\n", counter);
        counter++;
    }
    printf("Done!:  %f\n", counter);
    return 0;
}