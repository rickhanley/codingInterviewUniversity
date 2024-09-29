#include <stdio.h>
#include <stdlib.h>
// #include <windows.h>
#include "bmp.h"

int main(void){
    
    // open the file and check for error
    FILE *inptr = fopen("millie.bmp", "rb");
    if (inptr == NULL){
        printf("Error opening file\n");
        return 1;
    };

    FILE *outptr = fopen("output.bmp", "wb");
    if (outptr == NULL)
    {
        fclose(inptr);
        printf("Could not create %s.\n", outptr);
        return 5;
    };

    // create an alias of the BITMPAFILEHEADER called bf
    BITMAPFILEHEADER bf;
    // store at the address of bf: 
    // the sizeof the BITMAPFILEHEADER * 1 from inptr
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // create an alias of the BITMAPINFOHEADER called bi
    BITMAPINFOHEADER bi;
    // store at the address of bi: 
    // the sizeof the BITMAPINFOHEADER * 1 from inptr
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // printf("sizeof: %d\n", sizeof(BITMAPFILEHEADER));
    // printf("bfType: %x\n", bf.bfType);
    // printf("bfOffBits: %u\n", bf.bfOffBits);
    // printf("bfbfSize: %u\n", bf.bfSize);
    // printf("biSize: %u\n", bi.biSize);
    // printf("biBitCount: %u\n", bi.biBitCount);
    // printf("biHeight: %u\n", bi.biHeight);
    // printf("biWidth: %u\n", bi.biWidth);
    // printf("biSizeImage: %u\n", bi.biSizeImage);
    // printf("biCompression: %u\n", bi.biCompression);


    // Ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        printf("Unsupported file format.\n");
        return 6;
    };

    // Get image dimensions
    int old_height = abs(bi.biHeight);
    int old_width = bi.biWidth;

    int new_width = 128;
    int new_height = 85;

    // Bitmpap file data MUST end on a 4 byte boundary
    // Set variables to enable the bitmap data to be read / written
    // of the required lengths
    int old_padding = (4 - (old_width * sizeof(RGBTRIPLE)) % 4) % 4;
    int new_padding = (4 - (new_width * sizeof(RGBTRIPLE)) % 4) % 4;

    // printf("new_height: %d     New_width: %d\n", new_height, new_width);

    bi.biWidth = new_width;
    bi.biHeight = new_height; // Keep the height negative for top-to-bottom pixel order
    bi.biSizeImage = new_width * new_height * sizeof(RGBTRIPLE);
    bf.bfSize = sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER) + bi.biSizeImage;

    // Write updated headers to output file
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // printf("bfType: %x\n", bf.bfType);
    // printf("bfOffBits: %u\n", bf.bfOffBits);
    // printf("bfbfSize: %u\n", bf.bfSize);
    // printf("biSize: %u\n", bi.biSize);
    // printf("biBitCount: %u\n", bi.biBitCount);
    // printf("biHeight: %u\n", bi.biHeight);
    // printf("biWidth: %u\n", bi.biWidth);
    // printf("biSizeImage: %u\n", bi.biSizeImage);
    // printf("biCompression: %u\n", bi.biCompression);

    RGBTRIPLE(*image)[old_width] = calloc(old_height, sizeof(RGBTRIPLE[old_width]));

    if (image == NULL)
    {
        printf("Not enough memory to store image.\n");
        fclose(outptr);
        fclose(inptr);
        return 7;
    }

    for (int i = 0 ; i < old_height; i++) {
        // printf("%d\n", i);
        for (int j = 0; j < old_width; j++) {
            fread(&image[i][j], sizeof(RGBTRIPLE), 1, inptr);
        }
    }

    RGBTRIPLE(*new_image)[new_width] = calloc(new_height, sizeof(RGBTRIPLE[new_width]));

    for (int i = 0; i < new_height; i++) {
        // printf("i: %d\n", i);
        
        for (int j = 0; j < new_width; j++) {
            // printf("j: %d\n", j);
            // Calculate the corresponding pixel in the original image
            int old_i = i * old_height / new_height;
            int old_j = j * old_width / new_width;
            // printf("old_i: %d\n", old_i);
            // printf("old_j: %d\n", old_j);
            new_image[i][j] = image[old_i][old_j];
        }
    }

    // for(int i = 0; i < 85; i++){
    //     for(int j = 0; j < 128; j++){
    //         printf("%d\n", new_image[i][j]);
    //     };
    // }


    for (int i = 0; i < new_height; i++) {
        fwrite(new_image[i], sizeof(RGBTRIPLE), new_width, outptr);
    }

    // printf("pixel readout check:   %d\n\n",image[100][100].rgbtBlue);
    // printf("pixel readout check:   %d\n\n",image[100]->rgbtGreen);
    // printf("pixel readout check:   %d\n\n",image[100]->rgbtRed);

    FILE *txtptr = fopen("data.txt", "w");
    if (txtptr == NULL)
    {
        fclose(txtptr);
        printf("Could not create data.txt\n");
        return 5;
    };

    for (int i = 0; i < new_height; i++){
        for (int j = 0; j < new_width; j++){
            fprintf(txtptr, "%d, ", new_image[i][j].rgbtRed);
            fprintf(txtptr, "%d, ", new_image[i][j].rgbtGreen);
            fprintf(txtptr, "%d, ", new_image[i][j].rgbtBlue);
        }
    };

    free(image);
    free(new_image);
    fclose(inptr);
    fclose(outptr);
    fclose(txtptr);
}