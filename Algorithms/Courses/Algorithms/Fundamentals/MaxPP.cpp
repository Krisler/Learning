#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxpairwise(const vector<int> *numb)
{
  int n = numb->size();
  int maxpair = 0;
  for (int first = 0; first < n; ++first)
  {
    for (int second = first + 1; second < n; ++second)
    {
      maxpair = std::max(maxpair, (numb->at(first) * numb->at(second)));
    }
  }
  return maxpair;
}

int main()
{
  // Take input data
  int n;
  cin >> n;
  vector<int> numbers(n);

  for (int i = 0; i < n; ++i)
  {
    cin >> numbers[i];
  }

  cout << maxpairwise(&numbers) << endl;

  return 0;
}