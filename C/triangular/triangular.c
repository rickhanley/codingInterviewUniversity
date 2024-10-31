#include <stdio.h>

int triangular(int num){
     
    if (num == 1){
        return 1;
    }

    else{
        return num + triangular(num - 1);
    };
}

int main(void){

    printf("Result: %d\n", triangular(3));

}