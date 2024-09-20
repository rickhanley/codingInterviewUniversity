#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define BUFFER_LENGTH 4

int main(void){

    FILE *fptr;
    fptr = fopen("list.txt", "r");

    if(fptr == NULL){
        printf("File opening error\n");
    };

    char buffer[BUFFER_LENGTH];
    int line_count = 0;

    while(fgets(buffer, BUFFER_LENGTH, fptr) != NULL){
        line_count++;
    };
    rewind(fptr);
    
    int *sorting_array = malloc(sizeof(int) * line_count);

    int counter = 0;
    while(fgets(buffer, BUFFER_LENGTH, fptr) != NULL){
        sorting_array[counter] = atoi(buffer);
        counter++;
    };
    rewind(fptr);
    

    // for(int i = 0; i < line_count; i++){
    //     printf("Array = %d\n",sorting_array[i]);
    // };

    int temp = 0;
    bool swaps = false;

    for(int i = 0; i < line_count; i++){
        swaps = false;
        for(int j = 0; j < line_count - i - 1; j++){
            if(sorting_array[j] > sorting_array[j + 1]){
                temp = sorting_array[j + 1];
                sorting_array[j + 1] = sorting_array[j];
                sorting_array[j] = temp;
                swaps = true;
            };
        };
        if(swaps == false){
            break;
        };
    };
    for(int i = 0; i < line_count; i++){
    };


    fptr = fopen("sorted_output.txt", "w");
    if(fptr == NULL) {
        printf("File output creation error\n");
        return 1;
    };

    int output_counter = 0;
    while(output_counter < line_count){
        fprintf(fptr, "%d\n", sorting_array[output_counter]);
        output_counter++;
    };


    fclose(fptr);
    free(sorting_array);

}