#include <algorithm>
#include <iostream>
#include <vector>
#include <cassert>

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

class TestOtherAlgorithms {
public:
    static void test() {
        vector<int> expectedResult = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
        {
            vector<int> result;
            sieveEratosthenes(100, result);
            assert(expectedResult == result);
            cout << "sieveEratosthenes passed tests\n";
        }
        {
            /*int expectedResult = 8;
            int result = *inter_search(&testArr[0], &testArr[testArr.size() - 1], 7);
            assert(expectedResult == result);
            cout << "inter_search passed tests\n";*/
        }
    }
};
