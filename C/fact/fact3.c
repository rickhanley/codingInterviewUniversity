#include <stdio.h>
#include <stdlib.h>

int fact(int x){
    if(x == 1){
        return 1;
    }
    else {
        return x * fact(x - 1);
    };
};

int main(void){

    FILE *fptr;

    fptr = fopen("numbers.txt", "r");
    char line[4];
    int number = 0;

    if(fptr == NULL){
        printf("File error\n");
    }
    else{
        while(fgets(line, sizeof(line), fptr) != NULL){
            number = atoi(line);

            printf("Factorial of %d is %d\n", number, fact(number));
        };
    };
    fclose(fptr);

    return 0;
}