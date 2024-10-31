char* longestCommonPrefix(char** strs, int strsSize) {
    
    // find shortest input string
    
    int shortest = strlen(strs[0]);
    int current_length = 0;
    int shortest_index = 0;
    
    for (int i = 0; i < strsSize; i++){
        int current_length = strlen(strs[i]);
        if (shortest < current_length) {
            continue;
        }
        else {
            shortest = current_length;
            shortest_index = i;
        }
        
    }
    printf("%d\n",shortest);
    printf("%d\n",shortest_index);
    
    char buffer[200];
    // char matching_string[200];
    int highest_index = 0;
    int number_of_matches = 0;
    int final_lowest_number_of_matches = shortest;
    
    
    // now we have the shortest length string
    // loop over it a + 1 character at a time and 
    // search for a match across the other
    // strings
    
    for (int i = 0; i < strsSize; i++){
        if (i == shortest_index){
            continue;
        }
        else{
            printf("looking at str index: %d and comparing with %d\n", i, shortest_index);
            for (int j = 0; j < shortest; j++){
                if (strs[i][j] == strs[shortest_index][j]){
                    number_of_matches++;
                    printf("%c with %c\n",strs[i][j] ,strs[shortest_index][j]);
                }
            }
            if (number_of_matches == 0){
                return "";
            }
            else if (final_lowest_number_of_matches > number_of_matches){
                final_lowest_number_of_matches = number_of_matches;
            }
            printf("final lowest number: %d\n", final_lowest_number_of_matches);
                
            }
        }    
    return strs[0];
}