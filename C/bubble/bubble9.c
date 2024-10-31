#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main (void){

    FILE *inptr = fopen("numbers.txt", "r");

    if (inptr == NULL){
        printf("File open error\n");
        return 1;
    };

    int list_length = 0;
    char buffer[6];

    while (fgets(buffer, 6, inptr) != NULL){
        list_length++;
    }

    int *myarray = malloc(sizeof(int) * list_length);

    printf("%d\n", list_length);

    rewind(inptr);

    for (int i = 0; i < list_length; i++){
        myarray[i] = atoi(fgets(buffer,6,inptr));
    };

    for (int i = 0; i < list_length; i++){
        printf("%d\n", myarray[i]);
    };

    int temp = 0;
    bool swaps = false;

    for (int i = 0; i < list_length; i++){
        swaps = false;
        for (int j = 0; j < list_length - 1 - i; j++){
            // printf("inner loop\n");
            if (myarray[j] > myarray[j + 1]){
                temp = myarray[j + 1];
                myarray[j + 1] = myarray[j];
                myarray[j] = temp;
                swaps = true;
            }
        }
        if (swaps == false){
            break;
        }
    }

    for (int i = 0; i < list_length; i++){
        printf("%d\n", myarray[i]);
    }


    free(myarray);
    fclose(inptr);
    return 0;
}