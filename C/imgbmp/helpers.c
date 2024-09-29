#include "helpers.h"
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int temp = 0;

    // loop over rows of image [i] and adjust each rgb triple [j] to greyscale
    // reemember each rgb triple is really just a pixel
    // output adjuted rgb triples - remember BGR order
    // BYTE  rgbtBlue;
    // BYTE  rgbtGreen;
    // BYTE  rgbtRed;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // check50 kicked out an error - this was determiend to be rounding related. So an rgb triple of 27, 28, 28
            // was coming out as 27 when it should have been 28.
            // Casting the average calculation of the rgb tiples to float resolved this
            temp =  round((float)(image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3);

            image[i][j].rgbtBlue = temp;
            image[i][j].rgbtGreen = temp;
            image[i][j].rgbtRed = temp;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Declare some variables to use as counters in the loops below
    int jcounter = 0;
    int kcounter = 0;

    // declare a temp array of size width of the RGBTRIPLE struct
    // so 600 wide image == 600 x 8 bytes
    RGBTRIPLE temp[width];

    // outer loop to iterate over rows from image array
    for (int i = 0; i < height; i ++)
    {
        // we need to re-set our jcounter and kcounter back to 0 manually
        // after each row iteration otherwise their value will exceed
        // the index of the image array
        jcounter = 0;
        kcounter = 0;

        // as we iterate over each row we need to copy the row data, starting from the
        // maximum value of j and counting down
        for (int j = width - 1; j >= 0; j--)
        {
            // printf("Width: %d    J Counter = %d\n", j, jcounter);

            temp[jcounter].rgbtBlue = image[i][j].rgbtBlue;
            temp[jcounter].rgbtGreen = image[i][j].rgbtGreen;
            temp[jcounter].rgbtRed = image[i][j].rgbtRed;
            jcounter++;
        }

        // now write the temporary data back to the image array
        // in reverse order thus reversing the image
        for (int k = 0; k < width; k++)
        {
            image[i][k].rgbtBlue = temp[kcounter].rgbtBlue;
            image[i][k].rgbtGreen = temp[kcounter].rgbtGreen;
            image[i][k].rgbtRed = temp[kcounter].rgbtRed;
            kcounter++;
        }
        // printf("I: %d\n", i);
    }
    return;
}

// Blur image
// loop over the 2d array in a nested loop rows vs columns
// for each index we need to look at the cells surrounding the index
// one row above through one row below and one column left and one column to the right
// So we use the i / j nested loop to give the "master" co-ordinate we are looking at.
//
// We then do another nested loop using k / l for the box blur rows and columns.
// The k / l nested loops are the 3 x 3 grid of the box blur
// k will start one row above (i -1) and l will start one column to the left (j - 1).
//
// Edges
// Because we are potenitally going to ask the program to look at pixels
// outside of the array (anything less than zero or greater than the height / width)
// we use the if statements to filter those out - basically any instruction
// to look at elements outside of the array bounds will now meet with
// continue and hence no action will be performed and the loop counters will
// iterate for the next available element and see if that meets the conditions

void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // declare variables
    // we're going to average the values of the R G B elements of pixels so we need
    // 3 variables to hold the totals of the R G B values we read in from the image array.
    // We alos need to keep track of how many pixels we did read in -
    // this is critcal for edge cases where we won't always read in a
    // 3 x 3 grid and will enable a proper average to be calculated
    int blue_sum = 0;
    int green_sum = 0;
    int red_sum = 0;
    int pixels_read = 0;

    // we also need an RGBTRIPLE struct to hold the new pixels averaged data
    RGBTRIPLE blurred[height][width];


    for (int i = 0; i < height; i++) // rows
    {
        for (int j = 0; j < width; j++) // columns
        {
            pixels_read = 0; // critical to reset this to zero here
            for (int k = i - 1; k < i + 2; k++) // mini rows of the 3 x 3
            {
                for (int l = j - 1; l < j + 2; l++) // mini columns of the 3 x 3
                {
                    // if to handle edge cases and filter out reads we shouldn't make
                    if ((k < 0 || k > height - 1) || (l < 0 || l > width - 1))
                    {
                        continue;
                    }
                    // else does the work of incrementing the pixel_read variable
                    // and also adds in any R G B values to the relevant R G B sum
                    // variable.
                    else
                    {
                        pixels_read++;
                        blue_sum += image[k][l].rgbtBlue;
                        green_sum += image[k][l].rgbtGreen;
                        red_sum += image[k][l].rgbtRed;
                        // printf("i: %d     j: %d       k: %d     l: %d      pixels read: %d    Blue Value per pix: %d    Blue_sum: %d\n", i, j , k, l, pixels_read, image[k][l].rgbtBlue, blue_sum);
                    }
                }
            }
            // Back outside the 3 x 3 grid loop structure we are now able to
            // calculate an average for the pixel given at the image[i][j] position.
            // This pixel needs to be stored in our blurred array at the same [i][j] position

            // printf("blue sum: %d    pixels_read: %d = %d\n", blue_sum, pixels_read, (int)round((float) blue_sum / pixels_read));

            blurred[i][j].rgbtBlue = ((int)round((float) blue_sum / pixels_read));
            blurred[i][j].rgbtGreen = ((int)round((float) green_sum / pixels_read));
            blurred[i][j].rgbtRed = ((int)round((float) red_sum / pixels_read));
            // printf("Before %d,    Average %d\n", image[i][j].rgbtBlue, blurred[i][j].rgbtBlue);

            // critical all the sum variables get reset back to zero here ready for the next
            // 3 x 3 (or smaller) grid calculation
            blue_sum = 0;
            green_sum = 0;
            red_sum = 0;
        }
    }

// nested loop to copy all blurred data back into the image array, matching [i][j] positions exactly.
    for (int i = 0; i < height ; i++)
    {
        for (int j = 0; j < width ; j++)
        {
            image[i][j] = blurred[i][j];
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // define Sobel kernels

    int Gxarray[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}}; // vertical kernel
    int Gyarray[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}}; // horizontal kernal

    // Define an intermediate RGBTRIPLE same size as the input image
    // too perform the algorithm on

    RGBTRIPLE intermediate_edges[height][width];

    // printf("Red    Green   Blue     image[][]\n");

    // Nested for loops to loop over the input image and copy all the
    // data to intermediate edges
    for (int i = 0; i < height; i++) // rows
    {
        for (int j = 0; j < width; j++) // columns
        {
            intermediate_edges[i][j].rgbtBlue = image[i][j].rgbtBlue;
            intermediate_edges[i][j].rgbtGreen = image[i][j].rgbtGreen;
            intermediate_edges[i][j].rgbtRed = image[i][j].rgbtRed;
            // printf("%d      %d      %d      [%d][%d]\n", intermediate_edges[i][j].rgbtRed, intermediate_edges[i][j].rgbtGreen, intermediate_edges[i][j].rgbtBlue, i, j);
        }
    }

    // printf("\n\n");

    // Declare variables to hold to calcs from the sobel aglorithm - one each per colour per kernel
    float Gx_Blue = 0, Gy_Blue = 0, Gx_Green = 0, Gy_Green = 0, Gx_Red = 0, Gy_Red = 0;

    // Decalre 2 variables to control the indexing for the 3 x 3 grid
    // These will run from -1 to 1
    int l = 0;
    int k = 0;

    // Declare 2 variables to control the indexing for the kernels
    // These run in lock step with l & k above but will always be
    // +1
    int kernel_X = 0;
    int kernel_Y = 0;

    // Variables to help debgugging
    // int loop_count = 0;
    // int calc_counter = 0;
    // int ineligible = 0;


    // Nested loop to read every pixel of the input image
    // For every [i][j] the k & l variables attempt to read
    // a 3 x 3 grid around the pixel. If statement first part
    // makes sure nothing out of bounds is read (anything less < 0)
    // This will deal with left and top edge. If second part (i + k > height -1 etc)
    // makes sure the right hand and bottom edge case is not over-run also.
    // Else statement picks up anythign that is an ELIGIBLE read i.e. in bounds
    // then we can perform the first part of the sobel calc by += 'ing all the
    // red, greens and blue values multiplied by the corresponding sobel core value



    for (int i = 0 ; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // ******** key printf
            // printf("image[%d][%d].rgbtRed: %d       rgbtGreen: %d       rgbtBlue: %d\n", i, j, image[i][j].rgbtRed, image[i][j].rgbtGreen, image[i][j].rgbtBlue);
            // ************This sections of code is the 3 x 3 grid i.e. 9 iterations********************

            for (k = -1, kernel_X = 0; k < 2; k++, kernel_X++)
            {
                for (l = -1, kernel_Y = 0; l < 2; l++, kernel_Y++)
                {
                    if ((i + k < 0 || j + l < 0) || (i + k > height - 1 || j + l > width - 1))
                    {
                        // ineligible++;
                        continue;
                    }
                    else
                    {
                        // printf("i:%d    j:%d\n",i, j );
                        // incremement the Gx_Blue, Gy_Blue etc here
                        // printf("i+K: %d   j + l: %d\n", i+k, j+l);
                        // printf("%d   %d\n", i, j);

                        Gx_Red += image[i + k][j + l].rgbtRed * Gxarray[kernel_X][kernel_Y];
                        Gy_Red += image[i + k][j + l].rgbtRed * Gyarray[kernel_X][kernel_Y];

                        Gx_Green += image[i + k][j + l].rgbtGreen * Gxarray[kernel_X][kernel_Y];
                        Gy_Green += image[i + k][j + l].rgbtGreen * Gyarray[kernel_X][kernel_Y];

                        Gx_Blue += image[i + k][j + l].rgbtBlue * Gxarray[kernel_X][kernel_Y];
                        Gy_Blue += image[i + k][j + l].rgbtBlue * Gyarray[kernel_X][kernel_Y];

                        // printf("image[%d][%d].rgbtRed: %d  GX: %d  GY: %d     rgbtGreen: %d  GX: %d  GY: %d       rgbtBlue: %d  GX: %d  GY: %d\n", i, j, image[i][j].rgbtRed, Gxarray[kernel_X][kernel_Y], Gyarray[kernel_X][kernel_Y], image[i][j].rgbtGreen, Gxarray[kernel_X][kernel_Y], Gyarray[kernel_X][kernel_Y], image[i][j].rgbtBlue, Gxarray[kernel_X][kernel_Y], Gyarray[kernel_X][kernel_Y]);

                        // **** key printf
                        // printf("GX += rgbtblue: %d * %d  = %d   GY += rgbtblue: %d * %d = %d\n", image[i+k][j+l].rgbtBlue, Gxarray[kernel_X][kernel_Y], image[i+k][j+l].rgbtBlue * Gxarray[kernel_X][kernel_Y], image[i+k][j+l].rgbtBlue, Gyarray[kernel_X][kernel_Y], image[i+k][j+l].rgbtBlue * Gyarray[kernel_X][kernel_Y] );
                        // *********************************************************************************************
                        // printf("Gx Blue: %f   Gy_Blue %f    Gx_Green: %f     Gy_Green: %f    Gx_Red: %f     Gy_Red: %f\n", Gx_Blue, Gy_Blue, Gx_Green, Gy_Green, Gx_Red, Gy_Red);
                        // calc_counter++;

                    }
                    // printf("at i:%d j:%d we are looking at k: %d l: %d   K_X: %d   K_Y: %d   image blue: %d   GX_Blue: %f, \n", i, j, i + k, j + l, kernel_X, kernel_Y, image[i + k][j + l].rgbtBlue, Gx_Blue);
                    // printf("");
                    // loop_count++;
                }
            }
            // printf("%f\n", Gx_Red);


            // result = (result > 255) ? 255 : result;

            // *************************end of 9 iterations****************************************

            // when we have the total for the 3 x 3 grid per coloured pixel
            // we can do the second part of the sobel calc that squares each pixel's Gx and Gy total
            // then adds them together and sqrts the result. This final value is the new value for
            // the original pixel at position [i][j]

            // Note the ternery operator to stop values running over the 255 rgb cap.
            // Also the use of round to make sure we round correctly to int values


            // printf("end of eligibile reads %d\n", loop_count);
            // loop_count = 0;
            // printf("%d   %d\n", i, j);
            // Calc for 1 pixel happens here
            intermediate_edges[i][j].rgbtBlue = round(sqrt((Gx_Blue * Gx_Blue) + (Gy_Blue * Gy_Blue)) > 255 ? 255 : sqrt((Gx_Blue * Gx_Blue) + \
                                                (Gy_Blue * Gy_Blue)));
            // printf("sqrt Blue: %f\n", sqrt((float) (Gx_Blue * Gx_Blue) + (Gy_Blue * Gy_Blue)) > 255 ? 255 : sqrt((float) (Gx_Blue * Gx_Blue) + (Gy_Blue * Gy_Blue)) );
            intermediate_edges[i][j].rgbtGreen = round(sqrt((Gx_Green * Gx_Green) + (Gy_Green * Gy_Green)) > 255 ? 255 : sqrt((\
                                                 Gx_Green * Gx_Green) + (Gy_Green * Gy_Green)));
            // printf("sqrt Green: %f\n", sqrt((float) (Gx_Green * Gx_Green) + (Gy_Green * Gy_Green)) > 255 ? 255 : sqrt((float) (Gx_Green * Gx_Green) + (Gy_Green * Gy_Green)));
            // printf("green: %f\n", sqrt((Gx_Green * Gx_Green) + (Gy_Green * Gy_Green)));
            intermediate_edges[i][j].rgbtRed = round(sqrt((Gx_Red * Gx_Red) + (Gy_Red * Gy_Red)) > 255 ? 255 : sqrt((Gx_Red * Gx_Red) + \
                                               (Gy_Red * Gy_Red)));
            // printf("sqrt Red: %f\n", sqrt((float) (Gx_Red * Gx_Red) + (Gy_Red * Gy_Red)) > 255 ? 255 : sqrt((float) (Gx_Red * Gx_Red) + (Gy_Red * Gy_Red)));
            // Key printf
            //************************************************************************
            // printf("i: %d      j: %d     Blue Calc:%d     Green Calc:%d       Red Calc:%d\n", i, j, (unsigned char) round(sqrt((Gx_Blue * Gx_Blue) + (Gy_Blue * Gy_Blue))), (unsigned char) round(sqrt((Gx_Green * Gx_Green) + (Gy_Green * Gy_Green))), (unsigned char) round(sqrt((Gx_Red * Gx_Red) + (Gy_Red * Gy_Red))));

            // printf("Red Calc:%d     Green Calc:%d       Blue Calc:%d\n", (unsigned char) sqrt((Gx_Red * Gx_Red) + (Gy_Red * Gy_Red)), (unsigned char)  sqrt((Gx_Green * Gx_Green) + (Gy_Green * Gy_Green)), (unsigned char) sqrt((Gx_Blue * Gx_Blue) + (Gy_Blue * Gy_Blue)));


            // reset all the Gx / Gy variables here ready for th enext 3 x 3 iteration
            // printf("%f\n", Gx_Red);
            Gx_Blue = Gy_Blue = Gx_Green = Gy_Green = Gx_Red = Gy_Red = 0;

        }
    }

//  printf("Red    Green   Blue     image[][]\n");

    // Key printfs
    // printf("Loop count: %d\n",loop_count);
    // printf("Ineligible reads: %d     counter = %d \n",ineligible, calc_counter);

    // printf("Loop countcount %d\n",loop_count);
    // printf("Ineligible reads %d     counter = %d \n",ineligible, calc_counter);
    // printf("Edges [0][0] Blue: %d     Red: %d     Green: %d\n", edges[0][0].rgbtBlue, edges[0][0].rgbtGreen, edges[0][0].rgbtRed);
    // printf("Edges [0][14] Blue: %d     Red: %d     Green: %d\n", edges[0][14].rgbtBlue, edges[0][14].rgbtGreen, edges[0][14].rgbtRed);


    // final nested loop to copy the new calulated data back to the image STRUCT for passing back to the
    // filter.c

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width ; j++)
        {
            image[i][j] = intermediate_edges[i][j];
            // printf("%d   %d\n", i, j);
        }
    }
    return;
}
