#include <stdio.h>
#include <locale.h>

int main(void){
    (setlocale(LC_ALL, "en_US.UTF-8")).

    char buffer[512];

    FILE* infile = fopen("frankenstein.txt", "r");

    while(fgets(buffer, sizeof(buffer), infile)){
        printf("%s", buffer);
    }

    return 0;
}