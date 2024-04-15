#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
  void merge(vector<int> &num1, int m, vector<int> &num2, int n)
  {
    int index1 = m - 1;
    int index2 = n - 1;
    int maxIndex = m + n - 1;

    while (index1 >= 0 && index2 >= 0)
    {
      if (num1[index1] > num2[index2])
      {
        num1[maxIndex--] = num1[index1--];
      }
      else
      {
        num1[maxIndex--] = num2[index2--];
      }
    }

    while (index2 >= 0)
    {
      num1[maxIndex--] = num2[index2--];
    }
  }
};

int main()
{
  vector<int> nums1 = {1, 2, 3, 0, 0, 0};
  int m = 3;
  vector<int> nums2 = {2, 5, 6};
  int n = 3;
  Solution p;
  p.merge(nums1, m, nums2, n);

  // Output the merged array nums1
  for (int num : nums1)
  {
    cout << num << " ";
  }
  cout << endl;

  return 0;
}