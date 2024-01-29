/*This solution uses a dynamic programming approach to build a 2D array (dp) where dp[i][j] is true if the substring from index i to index j is a palindrome.
The algorithm counts palindromic substrings by considering substrings of length 1, 2, and 3 or more. The time complexity is O(n^2), where n is the length of the input string.*/
#include <iostream>
#include <vector>

class Solution
{
public:
    int countSubstrings(std::string s)
    {
        int n = s.length();
        int count = 0;

        // Create a 2D DP array to store whether a substring is a palindrome or not
        std::vector<std::vector<bool>> dp(n, std::vector<bool>(n, false));

        // All individual characters are palindromes
        for (int i = 0; i < n; ++i)
        {
            dp[i][i] = true;
            ++count;
        }

        // Check palindromes for substrings of length 2
        for (int i = 0; i < n - 1; ++i)
        {
            if (s[i] == s[i + 1])
            {
                dp[i][i + 1] = true;
                ++count;
            }
        }

        // Check palindromes for substrings of length 3 or more
        for (int len = 3; len <= n; ++len)
        {
            for (int i = 0; i <= n - len; ++i)
            {
                int j = i + len - 1;
                if (s[i] == s[j] && dp[i + 1][j - 1])
                {
                    dp[i][j] = true;
                    ++count;
                }
            }
        }

        return count;
    }
};

int main()
{
    Solution solution;

    // Example 1
    std::string s1 = "abc";
    std::cout << "Example 1: " << solution.countSubstrings(s1) << std::endl;

    // Example 2
    std::string s2 = "aaa";
    std::cout << "Example 2: " << solution.countSubstrings(s2) << std::endl;

    return 0;
}
