#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    string minWindow(string s, string t)
    {
        // Initialize the counter maps for characters in t and the current window
        unordered_map<char, int> charCountT, charCountWindow;

        // Populate the counter map for characters in t
        for (char ch : t)
        {
            charCountT[ch]++;
        }

        // Initialize variables to keep track of the window boundaries
        int start = 0, end = 0;

        // Variables to keep track of the minimum window substring
        int minLen = INT_MAX;
        int minStart = 0;

        // Variable to keep track of the number of characters in t that are yet to be included in the window
        int requiredChars = t.length();

        // Loop through the string s using the end pointer
        while (end < s.length())
        {
            // Check if the current character is a part of t
            if (charCountT.find(s[end]) != charCountT.end())
            {
                charCountWindow[s[end]]++; // Increment the count of the character in the current window
                if (charCountWindow[s[end]] <= charCountT[s[end]])
                {
                    // If including this character satisfies a requirement from t
                    requiredChars--;
                }
            }

            // Try to minimize the window by moving the start pointer
            while (requiredChars == 0)
            {
                // Update the minimum window substring if a smaller window is found
                if (end - start + 1 < minLen)
                {
                    minLen = end - start + 1;
                    minStart = start;
                }

                // Move the start pointer to the right to exclude characters
                if (charCountT.find(s[start]) != charCountT.end())
                {
                    charCountWindow[s[start]]--; // Decrement the count of the character in the current window
                    if (charCountWindow[s[start]] < charCountT[s[start]])
                    {
                        // If excluding this character breaks a requirement from t
                        requiredChars++;
                    }
                }
                start++;
            }

            // Move the end pointer to the right to expand the window
            end++;
        }

        // Check if a valid window was found
        if (minLen == INT_MAX)
        {
            return "";
        }
        else
        {
            return s.substr(minStart, minLen);
        }
    }
};

int main()
{
    Solution solution;

    // Example 1
    string s1 = "ADOBECODEBANC";
    string t1 = "ABC";
    cout << "Example 1: " << solution.minWindow(s1, t1) << endl;

    // Example 2
    string s2 = "a";
    string t2 = "a";
    cout << "Example 2: " << solution.minWindow(s2, t2) << endl;

    // Example 3
    string s3 = "a";
    string t3 = "aa";
    cout << "Example 3: " << solution.minWindow(s3, t3) << endl;

    return 0;
}
