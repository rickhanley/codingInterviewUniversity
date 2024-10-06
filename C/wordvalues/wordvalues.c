#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "functions.h"

int main(void){

    FILE *inptr = fopen("wordlist.txt", "r");

    if(inptr == NULL){
        printf("Input file error\n");
        return 1;
    };

    FILE *outptr = fopen("wordvalues.txt", "w");

    if(outptr == NULL){
        printf("Output file error\n");
        return 2;
    }

    char buffer[50];
    int word_total_from_function = 0;
    int largest = 0;
    char *largest_word;

    while(fgets(buffer, sizeof(buffer), inptr) != NULL){
        word_total_from_function = word_total(buffer);
        // printf("%d\n", word_total_from_function);
        fprintf(outptr, "%d\n", word_total_from_function);
        if (largest < word_total_from_function){
            largest = word_total_from_function;
            printf("%s\n", buffer);
        };
    };

    fclose(inptr);
    fclose(outptr);

    int word_total = 0;
    char letters[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

    char *test_word = "rick";

    for(int i = 0; i < strlen(test_word); i++){
        for(int j = 0; j < 26; j++){
            if(test_word[i] == letters[j]){
                word_total += j + 1;
                continue;
            };
        };
    }
    printf("largest word: %d  \n", largest);
    printf("TOTAL: %d\n", word_total);
    printf("\n");


    return 0;
}