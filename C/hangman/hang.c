#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include "functions.h"

#define GUESSES 10

int main(void){

    char *random_word = word_selector();
    char validated_guess = '\0';
    int word_length = strlen(random_word) - 1;
    int word_length_copy = word_length;
    // printf("word_legth at assignement: %d\n", word_length);
    int remaining_guesses = word_length + 2;
    bool game_over = false;
    int remaining_letters = word_length;
    char used_letters[26] = {"\0"};
    // printf("RL: %d\n", *remaining_letters);

    for(int i = 0; i < word_length; i++){
        random_word[i] = tolower(random_word[i]);
    };

    char *game_array = malloc(sizeof(char) * (word_length + 1));
    for(int i = 0; i < word_length; i++){
        game_array[i] = '_';
    }
    game_array[word_length] = '\0';
    
    char guess = ' ';
    
    while(game_over == false){
        // print_game(remaining_guesses);
        printf("top of game loop remaining_guesses: %d, remaining_letters: %d\n", remaining_guesses, remaining_letters);
        print_game(&remaining_guesses, &word_length, used_letters);
        validated_guess = validate_guess(guess, used_letters);
        guess_check(validated_guess, word_length, random_word, game_array, &remaining_letters, used_letters, &remaining_guesses);
    
        if(remaining_guesses == 0){
            printf("remaing guesses == 0\n");
            game_over = true;
            printf("\033[31mGame Over - out of guesses!\033[0m\n");
            printf("Word was: %s\n", random_word);
        };
        if(remaining_letters == 0){
            game_over = true;
            printf("\033[32mYou Won!\033[0m\n");
        };
    };
free(random_word);
};