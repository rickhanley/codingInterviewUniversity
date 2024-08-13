#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

bool is_empty (char *string){
    if(strlen(string) == 0) {
        return true;
    }
    else 
    return false;
}

char *return_char(char *input_string, char new_char){

    int existing_string_length = strlen(input_string);

    char *new_string = malloc(sizeof(existing_string_length + 1));
    new_string[0] = new_char;

    for(int i = 1; i <= existing_string_length; i++){
        new_string[i] = input_string[i-1];
    }
    new_string[existing_string_length] = '\0';
    
    return new_string;
}

int main(void) {  

    char *my_string = "Hello Rick";

    printf("%s\n", my_string);
    printf("%c\n",my_string[5]);
    printf("%d\n", strlen(my_string));

    printf("is empty: %d\n", is_empty(my_string));
    // printf("return_char: %s\n", return_char(my_string, 'X'));
    my_string = return_char(my_string, 'b');
    my_string = return_char(my_string, 'x');
    my_string = return_char(my_string, 'P');
    my_string = return_char(my_string, 'w');
    printf("return_char: %s\n", my_string);

    return 0;
}

