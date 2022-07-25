#include "sorting.hpp"
#include "sorting.cpp"
#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    cout << "Hello, World!\n";
    int moveCount = 0;
    int compCount = 0;
    int arraySize = 4;
    int *a = new int[arraySize];
    
    for ( int i = 0; i < arraySize; i++){
        a[i]= rand() % 20 + 1; // generate random number between 1 and 20
    }
    
    int first = a[0];
    int last = a[arraySize];
    insertionSort( a,first, last, compCount, moveCount);
    
    for ( int i = 0; i < arraySize; i++){
        cout << a[i];
    }
    
    return 0;
}
