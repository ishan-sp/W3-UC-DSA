#include<iostream>
using namespace std;
int lenA;

void selectionSort(int arr[], int top) {
    for(int i = 0; i < top; i++) {
        for(int k= i; k < top; k++) {
            if (arr[k] < arr[i]) {
                //swap
                int temp = arr[i];
                arr[i] = arr[k];
                arr[k] = temp;
            }
        }
    }
}


int main() {
    int a[] = {1,65,23,45,67,3,1,543,512,45,56};
    lenA = sizeof(a)/sizeof(int);
    cout << "Length of the array is " << lenA << endl;
    cout << "Before sorting :" << endl;
    for(int j = 0; j < lenA; j++) {
        cout << a[j] << " ";
    }
    cout << endl;
    selectionSort(a, lenA);
    cout << "After sorting" << endl;
    for(int i = 0; i < lenA; i++) {
        cout << a[i] << " ";
    }


    return 0;
}