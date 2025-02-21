#include <bits/stdc++.h>

using namespace std;
class Solution
{
public:
    const int MOD = 1000000007;

    int calculateWays(int wordLen, int maxVowels)
    {
        if (maxVowels == 0)
        {
            long long ans = 1;
            for (int i = 0; i < wordLen; i++)
            {
                ans = (ans * 21LL) % MOD;
            }
            return (int)ans;
        }

        vector<vector<long long>> dp(wordLen + 1, vector<long long>(maxVowels + 1, 0));
        dp[0][0] = 1;

        for (int i = 0; i < wordLen; i++)
        {
            for (int j = 0; j <= maxVowels; j++)
            {
                if (dp[i][j] == 0)
                    continue;
                dp[i + 1][0] = (dp[i + 1][0] + dp[i][j] * 21LL) % MOD;
                if (j < maxVowels)
                {
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j] * 5LL) % MOD;
                }
            }
        }

        long long ans = 0;
        for (int j = 0; j <= maxVowels; j++)
        {
            ans = (ans + dp[wordLen][j]) % MOD;
        }
        return (int)ans;
    }
};

int main()
{
    Solution sol;

    // Test Case 1
    cout << "Test Case 1 (wordLen=1, maxVowels=0): " << sol.calculateWays(1, 0) << " (Expected: 21)" << endl;

    // Test Case 2
    cout << "Test Case 2 (wordLen=1, maxVowels=1): " << sol.calculateWays(1, 1) << " (Expected: 26)" << endl;

    // Test Case 3
    cout << "Test Case 3 (wordLen=2, maxVowels=2): " << sol.calculateWays(2, 2) << " (Expected: 676)" << endl;

    // Test Case 4
    cout << "Test Case 4 (wordLen=2, maxVowels=0): " << sol.calculateWays(2, 0) << " (Expected: 441)" << endl;

    // Test Case 5
    cout << "Test Case 5 (wordLen=4, maxVowels=1): " << sol.calculateWays(4, 1) << " (Expected: 412776)" << endl;

    // Test Case 6
    cout << "Test Case 6 (wordLen=4, maxVowels=2): " << sol.calculateWays(4, 2) << " (Expected: 451101)" << endl;

    return 0;
}