#pragma once
#include <iostream>
#include <vector>

using namespace std;

    int maxSubArray(vector<int>& nums) {
        std::vector<int> dptable = std::vector<int>();
        if (nums.size() < 2) return nums[0];
        dptable.push_back(nums[0]);
        int global_max = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            int local_max = nums[i]; 
            int value = max(dptable[i-1] + nums[i], local_max);
            if (value > local_max) {
                local_max = value; 
            }
            dptable.push_back(local_max);
            if (local_max > global_max) {
                global_max = local_max; 
            }
        }
        return global_max;
    }
    
int main(){
    int arr[] = {-2,1,-3,4,-1,2,1,-5,4};
    auto newVec = vector<int>(arr, arr + sizeof(arr) / sizeof(arr[0]));
    cout <<  maxSubArray(newVec) << endl; 
}