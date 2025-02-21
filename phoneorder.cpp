#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int phoneCalls(vector<int> start, vector<int> duration, vector<int> volume)
    {
        int n = start.size();
        if (n == 0)
            return 0;

        // Create an index array representing the original positions.
        vector<int> idx(n);
        for (int i = 0; i < n; i++)
        {
            idx[i] = i;
        }

        // Sort indices based on finish time (start[i] + duration[i]).
        sort(idx.begin(), idx.end(), [&](int a, int b)
             { return (start[a] + duration[a]) < (start[b] + duration[b]); });

        // Precompute finish times for the sorted calls.
        vector<int> finish(n);
        for (int i = 0; i < n; i++)
        {
            finish[i] = start[idx[i]] + duration[idx[i]];
        }

        // dp[i] stores the maximum volume obtainable using the first i+1 sorted calls.
        vector<int> dp(n, 0);
        dp[0] = volume[idx[0]]; // Base case: take the first call.

        // Fill dp array.
        for (int i = 1; i < n; i++)
        {
            // Option 1: Include the current call.
            int includeCurrent = volume[idx[i]];
            int lastNonOverlap = findLastNonOverlapping(idx, start, finish, i);
            if (lastNonOverlap != -1)
            {
                includeCurrent += dp[lastNonOverlap];
            }

            // Option 2: Exclude the current call.
            dp[i] = max(dp[i - 1], includeCurrent);
        }

        return dp[n - 1];
    }

private:
    // Binary search helper: finds the last index in sorted order (by finish time)
    // where the call finishes at or before the call at position 'index' starts.
    int findLastNonOverlapping(const vector<int> &idx, const vector<int> &start,
                               const vector<int> &finish, int index)
    {
        int low = 0, high = index - 1;
        int ans = -1;
        int currentStart = start[idx[index]];

        while (low <= high)
        {
            int mid = (low + high) / 2;
            if (finish[mid] < currentStart)
            {
                ans = mid;
                low = mid + 1;
            }
            else
            {
                high = mid - 1;
            }
        }

        return ans;
    }
};

int main()
{
    // Sample Test Case:
    // Input: start = [10, 5, 15, 18, 30]
    //        duration = [30, 12, 20, 35, 35]s
    //        volume = [50, 51, 20, 25, 10]
    // Expected Output: 76
    vector<int> start = {10, 5, 15, 18, 30};
    vector<int> duration = {30, 12, 20, 35, 35};
    vector<int> volume = {50, 51, 20, 25, 10};

    Solution sol;
    int result = sol.phoneCalls(start, duration, volume);
    cout << "Output: " << result << "\n"; // Expected output: 76

    return 0;
}
