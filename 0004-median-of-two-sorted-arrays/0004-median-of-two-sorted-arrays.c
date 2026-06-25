#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

float findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int* merged = (int*)malloc((nums1Size + nums2Size) * sizeof(int));
    memcpy(merged, nums1, nums1Size * sizeof(int));
    memcpy(&merged[nums1Size], nums2, nums2Size * sizeof(int));

    qsort(merged,(nums1Size + nums2Size),sizeof(int),compare);

    int length = nums1Size + nums2Size;
    if (length % 2 == 0) {
        return ((float)merged[length / 2 - 1] + (float)merged[length / 2]) / 2.0;
    } else {
        return (float)merged[length / 2];
    }

    free(merged);
}
