#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));
    if (!result) return NULL;

    int i;
    for (i = 0; i < numsSize; i++) {
        int complement = target - nums[i];
        int j;
        for (j = 0; j < i; j++) {
            if (nums[j] == complement) {
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }

    free(result);
    *returnSize = 0;
    return NULL;
}
