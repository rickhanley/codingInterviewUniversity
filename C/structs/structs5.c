#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){

    typedef struct {
        char *name;
        int age;
    } Person;

    // Person person1;

    
    
    Person array[10];

    array[0].name = "Rick";
    array[0].age = 48;

    // array[0] = &person1;

    if (strcmp(array[0].name, "Rick") == 0){
        printf("This is rick\n");
    }

    printf("%d\n" ,sizeof(array));

    printf("%s   %d", array[0].name, array[0].age);
}