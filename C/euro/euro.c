#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){

    FILE *fptr;
    char buffer[120];

    int tallies[50] = {0};
    int bonus[12] = {0};
    int win = 0;
    int total_wins = 0;
    int largest_win;
    int winners[2000]={0};

    fptr = fopen("euro.txt", "r");

    while(fgets(buffer, 70, fptr) != NULL){
        char *token = strtok(buffer, ",");
        int column = 0;
        int temp = 0;

        // printf("buffer: %s\n", buffer);
        column = 0; 
        while (token != NULL) {
            column++;
            
            int num = atoi(token); // Convert token to int once
            // printf("num: %d\n", num);

            // Check if the number is within the expected range
            if (num >= 1 && num <= 50) {

                // Tally the count for the corresponding number
                if (column >= 5 && column <= 10) {
                    tallies[num - 1] += 1;
                    // printf("num: %d goes in index[num -1] : %d  token: %d\n", num, num - 1, token);
                }
                if (column >= 11 && column <= 12) {
                    bonus[num - 1] += 1;
                    // printf("num: %d goes in index[num -1] : %d  token: %d\n", num, num - 1, token);
                }
                if (column == 14) {
                    win = atoi(token);
                    total_wins += win;
                    if (largest_win < win){
                        largest_win = win;
                    }

                    // printf("winwinwinwinwinwinwinwinwinwinwinwinwinwinwinwinwinwinwin\n");
                };
            }
            token = strtok(NULL, ","); // token is updated with the next part of the string
        };
    };

    fclose(fptr);

    for(int i = 0; i < 50; i++){
        // printf("i: %d\n", i);
        printf("%2d: [%d] ", i + 1, tallies[i] );
        if((i + 1) % 5 == 0 && i != 0){
            printf("\n");
        }
    };

    printf("\n");

    for(int i = 0; i < 12; i++){
        // printf("i: %d\n", i);
        printf("%2d: [%d] ", i + 1, tallies[i] );
            if((i + 1) % 5 == 0 && i != 0){
                printf("\n");
        };
    };

    printf("\n");

    printf("Total win: %d    %d\n", total_wins, largest_win);
    return 0;
};