// my_functions.h
#ifndef FUNCTIONS_H
#define FUNCTIONS_H

// Function prototype (declaration)
char *word_selector();
int print_game(int *remaining_guesses, int *remaining_letters, char *used_letters);
char validate_guess(char guess, char *used_letters);
int guess_check(char guess, int word_length, char *random_word, char *game_array, int *remaining_letters, char *used_letters, int *remaining_guesses);
bool repeated_use_check(char guess, char *used_letters);
#endif
