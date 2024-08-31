// towers of hanoi
#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>

bool end_condition(int *array);
bool is_column_empty(int arr[3][3], int current_tower, int tower_height);
int get_top_disc(int *array, int tower_height, int *top_disc_index);
// int piece_count(int *array);
// int top_piece_value(int *array);


int main(void){

    bool column_empty = false;

    int towers[3][3] = {
        {3,2,1},
        {0,0,0},
        {3,2,1}
    };

    int tower_height = sizeof(towers[0]) / sizeof(int);
    // printf("tower_height: %d\n", tower_height);


    int while_counter = 0;
    int column_empty_or_not = 0;
    int base_disc = 0;
    int *top_disc_index = malloc(sizeof(int));

    if(top_disc_index == NULL){
        printf("Malloc issue\n");
        return 1;
    };

    int main_while_loop_counter = 0;
    int break_out_counter = 0;
    while(main_while_loop_counter < 2 && end_condition(towers[2]) != true){
        printf("main while loop: %d\n", main_while_loop_counter);
        main_while_loop_counter++;
        if(main_while_loop_counter == 2){
            main_while_loop_counter = 0;
            break_out_counter++;
        }
        
        if(break_out_counter == 10){
            printf("break_out_counter: %d\n", break_out_counter);
            break;
        }
    }

    for(int i = 0; i < tower_height; i++){
        // printf("Column %d is empty: %d\n", i, is_column_empty(towers, tower_height, i));
        column_empty_or_not = is_column_empty(towers, tower_height, i);
        if(column_empty_or_not != 1){
            base_disc = get_top_disc(towers[i], tower_height, top_disc_index);
            printf("Top disc: %d at index: %d\n", base_disc, *top_disc_index);
        }
    };

    // end_condition(towers[2]);
    free(top_disc_index);
    return 0;
}

bool is_column_empty(int arr[3][3], int tower_height, int current_tower){
    printf("tower height: %d     current_tower: %d\n", tower_height, current_tower);
    int top_piece = 0;
    // printf("current_tower: %d\n", current_tower);
    if(arr[current_tower][0] == 0 && arr[current_tower][1] == 0 && arr[current_tower][2] == 0){
        // printf("%d   %d   %d\n", arr[current_tower][0], arr[current_tower][1], arr[current_tower][2]);
        return true;
    }
    else {
        return false;
    }
    
};


bool end_condition(int *array) {
    if(array[0] != 3 && array[1] != 2 && array[2] != 3){
        printf("Not done\n");
        return false;
    }
    return true;
};
// Get top disc
// is passed the array representing the colum we're looking at
// loops decrementally looking for first non zero value and returns it
// also updates the *top_disc_index pointer to capture the index
// of where the disc was. Returns 0 if no discs found.
int get_top_disc(int *array, int tower_height, int *top_disc_index){
    // printf("tower_height: %d\n", tower_height);
    for(int i = tower_height - 1; i >=0; i--){
        printf("i: %d\n", i);
        if(array[i] != 0){
            *top_disc_index = i;
            return array[i];
        };
    };
    return 0;
};

