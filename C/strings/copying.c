#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(void) {

    char *original_string;
    original_string = "A simple text string";

    printf("Orignal string strlen(): %d\n", strlen(original_string));

    char *copied_string = malloc(strlen(original_string) + 1);
    strcpy(copied_string, original_string);
    printf("original string size: %d\n", strlen(original_string));
    printf("copied string size: %d\n", strlen(copied_string));
    return 0;
}