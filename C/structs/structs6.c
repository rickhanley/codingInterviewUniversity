#include <stdio.h>

typedef struct{
    int age;
    int weight;
} Person;


int main (void){

    Person person1;

    person1.age = 49;
    person1.weight = 93;

    printf("age: %d   weight: %d\n", person1.age, person1.weight);

    return 0;
}