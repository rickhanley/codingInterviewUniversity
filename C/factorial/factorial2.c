#include <stdio.h>

int fact(int x);

int main(void){

    int input = 5;

    printf("fact(%d) = %d\n",input, fact(input));

    return 0;

}

int fact(int x){

    if(x == 1){
        return 1;
    }
    else{
        return x * fact(x - 1);
    }
}
