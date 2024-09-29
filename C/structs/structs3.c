#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void){

    typedef struct {
        char name[50];
        int age; 
    } Person;

    Person person_array[15];

    strcpy(person_array[0].name, "Rick Hanley");
    person_array[0].age = 48;

    printf("person_array[0].name: %s\n", person_array[0].name);
    printf("person_age[0].age: %s\n", person_array[0].name);

    for (int i = 0; i < 15; i++) {
        if (person_array[i].age == 48) {
            printf("Name: %s\n", person_array[i].name);
        };
    };

    // strcpy(person1.name, "Dave Menne");

    // printf("person1.name: %s\n", person1.name);
    // printf("person1.age: %d\n", person1.age);
    return 0;
}