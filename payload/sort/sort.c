#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_LENGTH 100000

void generateArray(int arr[], int length) {
    srand(time(NULL));
    for (int i = 0; i < length; i++) {
        arr[i] = rand() % 100000;
    }
}

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quicksort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quicksort(arr, low, pi - 1);
        quicksort(arr, pi + 1, high);
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[ARRAY_LENGTH];
    generateArray(arr, ARRAY_LENGTH);
    quicksort(arr, 0, ARRAY_LENGTH - 1);
    printArray(arr, ARRAY_LENGTH);

    return 0;
}
