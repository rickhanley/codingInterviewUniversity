#include<stdio.h>

int main(int argc, char *argv[]) {
    printf("argc: %d\n", argc);

    for(int i = 0; i < argc; i++){
        printf("argument: %s\n", argv[i]);
    }

    return 0;
}