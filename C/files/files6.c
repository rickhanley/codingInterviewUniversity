#include <stdio.h>

int main(void){

    FILE* file = fopen("new_file.txt", "w");

    fprintf(file, "Hello!!!!\n");
    fclose(file);
}
