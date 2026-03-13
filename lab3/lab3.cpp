#include <iostream>
#include <new>
using namespace std;
// TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.



int* createArray(int size) {
    return new int[size];
}

void deleteArray(int* array) {
    delete[] array;
}

int findMax(int* arr, int size) {
    int max = *arr;
    for (int i = 0; i < size; i++) {
        if (max < *(arr + i)) {
            max = *(arr+i);
        }
    }
    return max;
}

void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
}

void swapValues(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void reverseArray(int* arr, int size) {
    int *first, *last;
    first = arr;
    last = (arr + size) - 1;
    while (first < last) {
        swapValues(first, last);
        first++;
        last--;
    }

}


int main() {
    cout << "Creating dynamic array..." << endl;
    cout << "Enter Array Size: ";
    int size;
    cin >> size;
    int* arr = createArray(size);
    cout << "Enter Values: ";
    for (int i = 0; i < size; i++) {
        cin >> *(arr + i);
    }
    printArray(arr,size);
    int max = findMax(arr, size);
    cout << " Maximum Element: " <<max << endl;
    cout << "---------------------------------------" <<endl;
    cout << "Swapping two elements" << endl;
    int a = 5;
    int b = 8;
    cout << "before swap: " <<endl;
    cout << "a: " <<a <<endl;
    cout<< "b: " << b << endl;
    swapValues(&a, &b);
    cout<< "after swap: " <<endl;
    cout << "a: " <<a <<endl;
    cout << "b: " << b << endl;
    cout << "---------------------------------------" <<endl;
    cout<<"Reversing Array..."<<endl;
    reverseArray(arr, size);
    cout << "Reversed Array: " <<endl;
    printArray(arr, size);
    cout << endl;
    cout << "---------------------------------------" <<endl;
    cout<<"Deleting Array..."<<endl;
    deleteArray(arr);
    cout<< "Memory Released Successfully."<<endl;


}

