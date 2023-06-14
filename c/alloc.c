#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    printf("Enter the size of array\n");
    scanf("%d", &n);
    int *pointer = (int *)malloc(n * sizeof(int));
    // int *pointer = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++)
    {
        printf("%d ", *(pointer + i));
    }
    free(pointer);
    printf("%d", *pointer);
    printf("\n");
}