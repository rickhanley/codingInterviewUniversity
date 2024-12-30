#include <stdio.h>

int main(void){

    // FILE pointer infile to get the return from fopen
    FILE* infile = fopen("input.txt", "r");
    // char buffer - REMEMBER not a char*
    char buffer[256];

    // While will loop because the return value of
    // fgets tells it when to stop i.e. when EOF
    // reached 
    while(fgets(buffer, sizeof(buffer), infile)){
        printf("%s",buffer);
    }

    fclose(infile);

    return 0;
}