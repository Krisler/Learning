#include <stdio.h>
#include <iostream>
using namespace std;

struct Rectangle
{
  int length;
  int breadth;
  char x;
};

int main()
{
  struct Rectangle r1 = {10, 5};

  printf("%ld\n", sizeof(r1));
  cout << r1.length << endl;
  cout << r1.breadth << endl;
  return 0;
}