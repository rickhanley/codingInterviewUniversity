// ****************************** Hangman *************************************
// 
// Simple hangman game implementation
// 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include "functions.h"

#define GUESSES 10

int main(void){
    

    char *random_word = word_selector(); // pointer to the random word selected
    char validated_guess = '\0'; // initilaise validate guess
    int word_length = strlen(random_word) - 1; // get lenght and knock off the \n
    int remaining_guesses = word_length; // set the guesses to match number of chars in word
    bool game_over = false; // to control game loop
    int remaining_letters = word_length; // initialise the remaining letters counter 
    char used_letters[26] = {"\0"}; // initilise the used letters array

    // make the random word lower case
    for(int i = 0; i < word_length; i++){
        random_word[i] = tolower(random_word[i]);
    };

    // allocate memory for game_array - allow for null terminator (+1)
    // initiliase the game_array with underscores
    // manually add in null terminator at the end
    char *game_array = malloc(sizeof(char) * (word_length + 1));
    for(int i = 0; i < word_length; i++){
        game_array[i] = '_';
    }
    game_array[word_length] = '\0';
    
    // initiliase guess
    char guess = ' ';
    printf("*****************************\n");
    printf("**********Hangman************\n");
    printf("*****************************\n\n");
    printf("A word of length: %d\n", word_length);
    // game loop - run while game over is false i.e. NOT won
    while(game_over == false){
        // printf("*****************************\n");
        // printf("A word of length: %d\n", word_length);
        // get game status with print_game()
        print_game(&remaining_guesses, &word_length, used_letters);
        // get a 
        validated_guess = validate_guess(guess, used_letters);
        guess_check(validated_guess, word_length, random_word, game_array, &remaining_letters, &remaining_guesses);
    
        if(remaining_guesses == 0){
            // printf("remaing guesses == 0\n");
            game_over = true;
            printf("\033[31m*******************************************\033[0m\n");
            printf("\033[31m********Game Over - out of guesses!********\033[0m\n");
            printf("\033[31m*******************************************\033[0m\n\n");
            printf("\033[31m* Word was: %s\n\033[0m\n", random_word);
            
        };
        if(remaining_letters == 0){
            game_over = true;
            printf("\033[32m******************************************\033[0m\n");
            printf("\033[32m**              You won!                **\033[0m\n");
            printf("\033[32m******************************************\033[0m\n");
        };
    };
// free the malloc'd space for random_word
free(random_word);
};