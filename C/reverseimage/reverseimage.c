#include <stdio.h>
#define RGBTRIPLE 3

int main(void){
    int width = 128;
    int height = 85;
    int rgbtriple = 3;
    int row_width = width * rgbtriple;

    printf("Row_width: %d\n", row_width);

    long total_size = width * height * rgbtriple;

    for(int i = 0; i < height; i = i + 1)
    {
        printf("i: %d\n", i);
        for (int j = total_size - (row_width * (i + 1)); j < total_size - (row_width * i); j = j + 3)
        {
            printf("j: %d\n", j);
        }
    }

    int old_width = 1600;
    int new_width = 1085;
    int old_padding = (4 - (old_width * rgbtriple % 4)) % 4;
    int new_padding = (4 - (new_width * rgbtriple % 4)) % 4;

    printf("sizeof RGB %d\n", rgbtriple);

    printf("old_padding: %d\n", old_padding);
    printf("new_padding = 4 - %d * %d = %d    %%4 = %d\n", new_width, rgbtriple, new_width * rgbtriple, new_width * rgbtriple % 4);

    printf("total_size: %d \n", total_size);

    // for(int i = 0; i < 8; i++){
    //     printf("%d %% 4 = %d\n", i, i % 4);
    // }


    return 0;
}