#include<stdlib.h>
#include<stdio.h>
#include<string.h>

int main(void) {

    char *original_string = "Hello, World!";
    char *copied_string = malloc(strlen(original_string) +1);
    if(copied_string == NULL) {
        printf("malloc failed. Exiting now!\n");
    }
    else {
    strcpy(copied_string, original_string);
    printf("sizeof original: %d\n", strlen(original_string));
    printf("This next line should show a matching value!\n");
    printf("sizeof copy: %d\n", strlen(copied_string));
    free(copied_string);
    }
   return 0;  
}