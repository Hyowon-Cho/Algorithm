#include <bits/stdc++.h>

using namespace std;

stack<int> s;

int main(void) {
  s.push(5);
  s.push(2);
  s.push(3);
  s.push(7);
  s.pop();
  while (!s.empty()) {
    cout << s.top() << ' ';
    s.pop();
  }
}
