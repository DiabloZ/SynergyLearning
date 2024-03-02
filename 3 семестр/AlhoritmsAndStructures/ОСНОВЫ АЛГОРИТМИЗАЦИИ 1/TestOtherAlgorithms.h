#include <algorithm>
#include <iostream>
#include <vector>
#include <cassert>
#include <valarray>

using namespace std;

void sieveEratosthenes(int num, vector<int> &result) {
    bool p[num + 10];
    for (int i = 2; i < num; ++i) {
        p[i] = true;
    }
    for (int x = 2; x < num; ++x) {
        if (p[x]) {
            for (int y = 2 * x; y < num; y += x) {
                p[y] = false;
            }
        }
    }
    for (int i = 2; i < num; ++i) {
        if (p[i]) {
            result.push_back(i);
        }
    }
}

bool isPrime(long x) {
    for (long i = 2; i * i <= x; ++i) {
        if (x % i == 0) {
            return false;
        }
    }
    return true;
}

string getPrimeString(int num) {
    string result = "Not T-prime\n";
    long long sq = sqrt(num);
    if (sq * sq == num && isPrime(sq)){
        result = "T-prime\n";
    }
    return result;
}

int nodRec(int x, int y) {
    if (x == 0 || y == 0) {
        return x + y;
    }
    return nodRec(y % x, x);
}

int nod(int x, int y) {
    while (x != 0 && y != 0) {
        if (x > y) {
            x %= y;
        } else {
            y %= x;
        }
    }
    return x + y;
}

int nok(int x, int y) {
    return x * y / nod(x, y);
}

class TestOtherAlgorithms {
public:
    static void test() {
        {
            vector<int> expectedResult = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
            vector<int> result;
            sieveEratosthenes(100, result);
            assert(expectedResult == result);
            cout << "sieveEratosthenes passed tests\n";
        }
        {
            int expectedResult1 = 0;
            int expectedResult2 = 0;
            int expectedResult3 = 1;
            bool result1 = isPrime(18);
            bool result2 = isPrime(20);
            bool result3 = isPrime(23);

            assert(expectedResult1 == result1);
            assert(expectedResult2 == result2);
            assert(expectedResult3 == result3);
            cout << "isPrime passed tests\n";
        }
        {
            string expectedResult = "T-prime\n";
            int num = 49;
            string result = getPrimeString(num);

            assert(expectedResult == result);
            cout << "getPrimeString passed tests\n";
        }
        {
            int expectedResult = 7;
            int expectedResultNok = 30;

            int result1 = nod(49, 56);
            int result2 = nodRec(49, 56);
            int result3 = nok(6, 10);

            assert(expectedResult == result1);
            assert(expectedResult == result2);
            assert(expectedResultNok == result3);

            cout << "nod && nodRec passed tests\n";
        }
        {
            int expectedResult = 3;

            int oranges = 6;
            int persons = 8;
            int result1 = oranges / nod(oranges, persons);

            assert(expectedResult == result1);

            cout << "oranges passed tests\n";
        }

    }


};
