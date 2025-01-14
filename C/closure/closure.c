#include <stdio.h>

int multiplier(int factor){
    return factor;
}

int answer(int x){
    return multiplier(6) * x;
}


int main(void){


printf("%d\n", answer(2));


}