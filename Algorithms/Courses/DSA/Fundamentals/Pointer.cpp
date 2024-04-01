#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
  int a = 10;
  int *p;
  p = &a;

  int A[5] = {2, 4, 6, 8, 10};
  int *v;
  p = A;

  // Array inside heap in C
  int *m;
  m = (int *)malloc(5 * sizeof(int));
  m[0] = 10;
  m[1] = 15;
  m[2] = 20;

  // Array inside heap in C++
  int *c;
  c = new int[5];

  cout << a << endl;
  printf("using pointer %d\n", *p);

  delete[] m; // C
  free(c);    // C++
  return 0;
}
