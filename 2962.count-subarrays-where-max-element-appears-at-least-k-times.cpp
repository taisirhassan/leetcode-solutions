/*
 * @lc app=leetcode id=2962 lang=cpp
 *
 * [2962] Count Subarrays Where Max Element Appears at Least K Times
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <ranges>
using namespace std;
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int max_num = ranges::max(nums);
        long long count = 0;
        int left = 0;
        int max_count = 0;
        for (int right = 0; right < n; ++right) {
            if (nums[right] == max_num) {
                max_count++;
            }
            while (max_count >= k) {
                count += n - right;
                if (nums[left] == max_num) {
                    max_count--;    
                }
                left++;
            }
        }
        return count;
    }
};
// @lc code=end

