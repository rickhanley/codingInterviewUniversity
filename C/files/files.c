#include <stdio.h>
#include <stdlib.h>

int main (void)
{
    FILE *fptr; // create a pointer to the FILE
    char buffer[100]; // create a small 10 char buffer to red into

    // point the file pointer to the file with fopen
    fptr = fopen("my_text_file.txt", "r"); 
    // if fopen is NOT NULL i.e. it#s been opened correctly
    // print a confirmation
    if(fptr != NULL){
        printf("File opened!\n");
    };

    // while loop
    // while the return value of fgets is NOT NULL the loop keeps running
    // fgets is writing to buffer, 10 chars at a time, reading from fptr
    while (fgets(buffer, sizeof(buffer), fptr) != NULL) {
        printf("%s", buffer);
    };

   fclose(fptr);

   return 0;
}