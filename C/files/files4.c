#include <stdio.h>

int main(void){

    FILE* file = fopen("my_file.txt", "w");
    if(file == NULL){
        printf("File allocation failed");
    }

    fprintf(file, "Hello, World!\n");
    fclose(file);

    return 0;
}