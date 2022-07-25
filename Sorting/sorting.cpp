#include "sorting.hpp"
#include <iostream>
using namespace std;

void insertionSort(int *arr, int first, int last, int &compCount, int &moveCount){
    
    
    int i = -1;
    int n = 0;
    while( i!=last){
        i= arr[n];
        n++; // number of elements in the array
    }
    for (int unsorted = 1; unsorted < n-1; ++unsorted) {
        
        int nextItem = arr[unsorted];
        int loc = unsorted;
        
        for (  ;(loc > 0) && (arr[loc-1] > nextItem); --loc)
            arr[loc] = arr[loc-1];
        
        arr[loc] = nextItem;
        compCount = 2;
        moveCount = 2;
    }
}
