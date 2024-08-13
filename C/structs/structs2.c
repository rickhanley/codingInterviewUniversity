#include<stdio.h>
#include<string.h>


int main(void) {
    typedef struct { // decalre typedef
        char name[50]; // Do not initialise within the struct
        int age; // Do not intiliase within the struct
    } Person; // this is the name of the type - use this to call instances.

    Person new_person_1; // call instance of Person called new_person_1

    // USE DOT notation
    strcpy(new_person_1.name, "Rick Hanley"); // use strcpy to copy
    new_person_1.age = 48; // assign age

    // Print to check
    printf("new_person_1.name: %s\nnew_person_1.age: %d\n", new_person_1.name, new_person_1.age);
}

