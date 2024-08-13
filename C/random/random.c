#include<stdio.h>
#include<time.h>
#include<stdlib.h>

int main(void){
    // srand(time(0));
    for(int i = 0; i < 5; i++){
        printf("%d\n", rand() % 10);
    }
    return 0;
}