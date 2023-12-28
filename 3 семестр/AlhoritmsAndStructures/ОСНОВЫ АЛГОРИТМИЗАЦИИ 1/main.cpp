#include <iostream>

int sum2(int n) {
    return (1 + n) * n / 2;
}

int sum1(int n) {
    int asn = 0;
    for (int i = 1; i <= n; ++i) {
        asn += i;
    }
    return asn;
}

using namespace std;

int main() {
    int n;
    cin >> n;
    cout << sum1(n) << endl;
    cout << sum2(n) << endl;
}


