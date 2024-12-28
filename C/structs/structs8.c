#include <stdio.h>

typedef struct {

    int age;
    int weight;
} Person;

int main(void){

    Person my_person;
    my_person.age = 89;
    my_person.weight = 55;

    printf("%d   %d", my_person.age, my_person.weight);

    return 0;

}