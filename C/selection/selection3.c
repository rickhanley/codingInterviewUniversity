#include <stdio.h>

int main(void){

    int inp[] = {5,1,3,2,4};

    int input_length = sizeof(inp) / sizeof(int);

    for(int i = 0; i < input_length -1; i++){
        printf("i: %d\n", i);
        int min = i;

        for(int j = i + 1; j < input_length; j++){
            printf("comparing if %d < %d\n", inp[j], inp[min]);
            if(inp[j] < inp[min]){
                printf("min gets: %d\n", inp[j]);
                min = j;
            }
        }
        printf("min on pass: %d\n", min);
        
        int temp = inp[i];
        inp[i] = inp[min];
        inp[min] = temp;
    }

    for(int i = 0; i < input_length; i++){
        printf("%d\n",inp[i]);
    }

    return 0;
}