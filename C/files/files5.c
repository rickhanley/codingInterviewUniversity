#include <stdio.h>

int main(void){

    FILE* file = fopen("Hello.txt", "w");
    if(file == NULL){
        printf("File opening error");
    };

    char my_array[] = {'H', 'e', 'l', 'l', 'o', '\0'};

    fprintf(file, my_array);
    fprintf(file, "\n");
    fclose(file);

    return 0;
}