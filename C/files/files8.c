#include <stdio.h>

int main(void){

    char buffer[64];

    FILE* infile = fopen("files8.txt", "w");

    for(int i = 0; i < 10; i++){
        fprintf(infile, "%d\n", i+1);
    }
    fclose(infile);

    infile = fopen("files8.txt", "r");

    while(fgets(buffer, sizeof(buffer), infile)){
        printf("%s", buffer);
    }

    fclose(infile);
}