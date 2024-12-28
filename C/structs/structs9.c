#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* name;
    int age;
}Person;

int main(void){

    const char* input_name = "Rick";

    Person my_person;
    my_person.age = 49;
    my_person.name = malloc(strlen(input_name) + 1);
    if(my_person.name == NULL){
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    strcpy(my_person.name, input_name);
    
    printf("%s is %d years old", my_person.name, my_person.age);

    return 0;
}