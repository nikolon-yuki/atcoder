#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{
    int N = 127;
    string ans = "";
    while (N >= 1)
    {
        if (N % 3 == 0)
            ans = "0" + ans;
        else if (N % 3 == 1)
            ans = "1" + ans;
        else if (N % 3 == 2)
            ans = "2" + ans;
        N = N / 3;
    }
    cout << ans << endl;
}
