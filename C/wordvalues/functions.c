#include <stdio.h>
#include <string.h>

int word_total(char *word){
    // printf("Incoming word: %s\n", word);

    int word_total = 0;
    char letters[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

    for(int i = 0; i < strlen(word); i++){
        for(int j = 0; j < 26; j++){
            if(word[i] == letters[j]){
                word_total += j + 1;
                continue;
            };
        };
    };
    // printf("word total: %d\n", word_total);
    // printf("TOTAL: %d\n", word_total);
    // printf("\n");
    return word_total;
};