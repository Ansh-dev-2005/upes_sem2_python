#include <stdio.h>
#include <stdlib.h>
int main(){
// This pointer will hold the// base address of the block created
int *ptr, *ptr1;
int n, i;
// Get the number of elements for the array
n = 5;
printf("Enter number of elements: %d\n", n);
// Dynamically allocate memory using malloc()
ptr = (int*)malloc(n * sizeof(int));
// Dynamically allocate memory using calloc()
ptr1 = (int*)calloc(n, sizeof(int));
// Check if the memory has been successfully
// allocated by malloc or not
if (ptr == NULL || ptr1 == NULL) {
    printf("Memory not allocated.\n");
    exit(0);
    }
    else {
        // Memory has been successfully allocated
        printf("Memory successfully allocated using malloc.\n");
        // Free the memory
        free(ptr);
        printf("Malloc Memory successfully freed.\n");
        // Memory has been successfully allocated
        printf("\nMemory successfully allocated using calloc.\n");
        // Free the memoryfree(ptr1);
        printf("Calloc Memory successfully freed.\n");
        }
        //Again allocate memory using malloc() from user input
        // printf("Enter number of elements: ");
        // scanf("%d", &n);
        // ptr = (int*)malloc(n * sizeof(int));
        // // Memory has been successfully allocated
        // printf("Memory successfully allocated using malloc.\n");
        // // Get the elements of the array
        // for (i = 0; i < n; ++i) {
        //     ptr[i] = i + 1;
        //     }
        //     // Print the elements of the array
        //     printf("The elements of the array are: ");
        //     for (i = 0; i < n; ++i) {
        //         printf("%d, ", ptr[i]);
        //         }
        //Again allocate memory using remalloc() from user input
        printf("Enter number of elements: ");
        scanf("%d", &n);
        ptr = (int*)realloc(ptr, n * sizeof(int));
        // Memory has been successfully allocated
        printf("Memory successfully allocated using realloc.\n");
        // Get the elements of the array
        for (i = 0; i < n; ++i) {
            ptr[i] = i + 1;
            }
            // Print the elements of the array
            printf("The elements of the array are: ");
            for (i = 0; i < n; ++i) {
                printf("%d, ", ptr[i]);
                }
                
                
        return 0;
     }

