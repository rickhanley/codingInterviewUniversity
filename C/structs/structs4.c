#include <stdio.h>
#include <string.h>

 typedef struct{
    char *name;
    int age;
} Person;

int main(void) {

    Person my_person;

    my_person.name = "Ricky";
    my_person.age = 48;

    printf("%s, %d\n", my_person.name, my_person.age);
    printf("%d\n",strlen(my_person.name));

    return 0;
}