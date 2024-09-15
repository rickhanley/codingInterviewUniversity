#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <sys/time.h>
#include <stdbool.h>
#include <ctype.h>

#define MAXLENGTH 50 // Constant to define maximum chbars in the buffer


//*****************************************************************************
//                          word_selector
//
// returns a string (char *) of a word chosen at random from the words in the 
// file
//
//
// ****************************************************************************
char *word_selector(void){

    FILE *fptr; // create a file pointer fptr
    char buffer[MAXLENGTH]; // create a character buffer of MAXLENGTH
    // open fptr in read only mode
    fptr = fopen("minlengthsix.txt" , "r");
    // Check for failure
    if(fptr == NULL) {
        printf("Wordlist error\n");
        return NULL;
    };
    // if we're good continue with the rest of the program.
    int word_count = 0; // variable to hold number of words in file

    // count words in the file
    while(fgets(buffer, sizeof(buffer), fptr) != NULL){
        word_count++;
    };

    rewind(fptr); // rewind to beginning of file
    
    // get a randome number in a larger range using bit shifting
    // rand() MAX SIZE is 32767
    struct timeval tv;
    gettimeofday(&tv, NULL);  // Get current time including microseconds
    srand((unsigned int)(tv.tv_sec ^ tv.tv_usec ^ word_count));
    long random_word_index = ((long)rand() << 15) | rand();
    random_word_index = random_word_index % word_count;


    char *selected_word; // string pointer to hold the word

    // loop over the file again this time up to the number
    // of the random word in the file
    for(int i = 0; i < random_word_index; i++){
        selected_word = fgets(buffer, MAXLENGTH, fptr);
    };

    fclose(fptr); // close the file
    
    // copy the word to chosen
    char *chosen = malloc(strlen(selected_word));
    strcpy(chosen, selected_word);

    return chosen; // return the chosen word

};

// check if the game is won

int print_game(int *remaining_guesses, int *remaining_letters, char *used_letters){
    
    printf("*****************************\n");
    printf("%d letter word\n", *remaining_letters);

    printf("Used Letters: ");

    for(int i = 0; i < 26; i++){
            if(used_letters[i] != '\0'){
                printf("%c ", used_letters[i]);
            };
        };
    printf("\n"); 
    printf("Remaining guesses (print_game): %d\n", *remaining_guesses);
    printf("\n");
printf("*****************************\n");
    return 0;
};

// returns false if letter entered hasn't been used before, true if it has
bool repeated_use_check(char guess, char *used_letters){
    // printf("Comparing guess: %c\n", guess);
    for(int i = 0; i < 26; i++){
        if(guess == used_letters[i]){
            return true;
        };
    };
    return false;
};

// Validate guess checks if the char is a letter
// and checks if the letter has been used previously

char validate_guess(char guess, char *used_letters){
        while(!isalpha(tolower(guess))){
            printf("first Enter a letter: ");
                scanf(" %c", &guess);
            if(repeated_use_check(guess, used_letters) == false){
                for(int i = 0; i < 26; i++){
                    if(used_letters[i] == '\0'){
                        used_letters[i] = guess;
                        break;
                    };
                };
                continue;
            }
            else {
                printf("Letter already used:\n");
                return('a');
            };
        };        
    return guess;
};

// checks if the letter is in the word
int guess_check(char guess, int word_length, char *random_word, char *game_array, int *remaining_letters, char *used_letters, int *remaining_guesses){
    printf("Remaining guesses receive check: %d\n", *remaining_guesses);
    bool match_flag = false;
    for(int i = 0; i < word_length; i++){
        if(random_word[i] == guess){
            game_array[i] = guess;
            (*remaining_letters)--;
            match_flag = true;
            printf("remaining letters: %d\n", *remaining_letters);
        };
        
    };
    if(match_flag == false){
        printf("No Match - remaining_guesses should decrememnt %d\n", *remaining_guesses);
        (*remaining_guesses)--;
        // printf("Remaining_guesses after decrement: %p\n", remaining_guesses);
        };
    
    
    for(int i = 0; i < word_length; i++){
        if(game_array[i] != '_'){
            printf("\033[32m%c\033[0m", game_array[i]);
            printf(" ");
        }
        else{
            printf("\033[31m%c\033[0m", game_array[i]);
            printf(" ");
        };
    };
    printf("\n\n\n");
};

