#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));
    if (!result){
        return NULL;
    }
    for (int i=0; i<numsSize; i++){
        int complement = target-nums[i];
        for (int j=0; j<i; j++){
            if (nums[j] == complement){
                result[0] = j;
                result[1] = i;
                *returnSize = 2;
                return result;
            }
        }
    }
    free(result);
    *returnSize = 0;
    return NULL;
}