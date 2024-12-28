#include <stdio.h>

int main(void){
    FILE *file = fopen("output.txt", "w");
    if (file == NULL){
        perror("Error opening file");
        return 1;
    }

    fprintf(file, "Hello World!\n");
    fclose(file);

    return 0;
}