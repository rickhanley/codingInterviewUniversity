#include <stdio.h>
#include <string.h>
#include<stdlib.h>

int main(void) {

    char *my_string;

    my_string = "My new string";

    printf(my_string);
    printf("\n");
    printf("length: %d\n", strlen(my_string));

    my_string = "My new string My new string My new string My new string";

    printf(my_string);
    printf("\n");
    printf("length: %d\n", strlen(my_string));

    char *my_malloc_string = malloc(sizeof(char) * 5);
    if (my_malloc_string == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    char *input_string = "Rick";
    strcpy(my_malloc_string, input_string);
    printf("%s\n", my_malloc_string);

    free(my_malloc_string);

    // printf("%s\n", my_malloc_string);


    // printf("my_malloc_string size: %d", sizeof(my_malloc_string));

    return 0;
}