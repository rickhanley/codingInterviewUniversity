#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]){

     FILE *fptr;
     int buffer;
     long counter = 0;
     char *filename = argv[1];

     if(argc != 2){
        printf("Usage: word-count filename.txt\n");
     }

     fptr = fopen(filename, "r");
     if(fptr == NULL){
        printf("File Error!\n");
     }
     else{

        while((buffer = fgetc(fptr)) != EOF){
            counter++;
            // printf("%c\n", buffer );
        }
        fclose(fptr);
        

        printf("Characters: %d\n", counter);
     };
    return 0;
}