#include <stdlib.h>
#include <stdio.h>


int main(void) {

    // open a pointer to "wordvalues.txt"
    FILE *inptr = fopen("wordvalues.txt", "r");
    // char buffer of 50 chars
    char buffer[50];

    // chekc file opens correctly
    if (inptr == NULL){
        printf("File Open Error\n");
    };

    // declare variable to hold the count of words in the file
    int total_entries = 0;
    // loop over the file contents incrementing total_entries
    while (fgets(buffer, sizeof(buffer), inptr) != NULL){
        total_entries++;
    };

    // declare my_array int pointer for holding 
    // the values from the wrods
    int *my_array = malloc(total_entries * sizeof(int));

    // printf("%d\n", total_entries);

    // bring file pointer back to start of file
    rewind(inptr);

    // declare counter so my_array can be indexed
    int counter = 0;
    // loop over the file again but this time
    // put the buffer contents (converted to an int)
    // into the my_array index given by counter
    while (fgets(buffer, sizeof(buffer), inptr) != NULL){
        my_array[counter] = atoi(buffer);
        counter++;
    };

    // close file
    fclose(inptr);

    // buble sort
    int swaps = 0;
    int temp = 0;
    
    for (int i = 0; i < total_entries; i++){
        swaps = 0;
        for (int j = 0; j < total_entries - 1 - i; j++){
            if (my_array[j] > my_array[j + 1]){
                temp = my_array[j + 1];
                my_array[j + 1] = my_array[j];
                my_array[j] = temp;
                swaps = 1;  
            };
        };
        if(swaps == 0){
            break;
        }
    };

    // print last element in array to find highest value
    printf("%d\n", my_array[total_entries - 1]);
    // free the array
    free(my_array);
    return 0;
}