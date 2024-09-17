#include <stdio.h>
#include <stdlib.h>

int main (void)
{
    FILE *fptr;
    char buffer[10];

    fptr = fopen("my_text_file.txt", "r");
    if(fptr != NULL){
        printf("File opened!\n");
    };

    while (fgets(buffer, sizeof(buffer), fptr) != NULL) {
        printf("%s", buffer);
    };

   fclose(fptr);

   return 0;
}