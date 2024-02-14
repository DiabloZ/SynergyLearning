#include <algorithm>
#include <iostream>
#include <vector>

int* bin_search(int* first, int* last, int x) {
    int sz = last - first + 1;
    int l = 0, r = sz;
    while (r - l > 1) {
        int m = (r + l) / 2;
        if (first[m] < x) {
            l = m;
        } else {
            r = m;
        }
    }
    if (l == r || r == sz || first[r] - x >= x - first[l]){
        return first + l;
    }
    return first + r;
}

int* inter_search(int* first, int* last, int x) {
    int sz = last - first + 1;
    int l = 0, r = sz;
    while (r - l > 1) {
        int m = l + (x - first[l]) * (r - l - 2) / (first[r - 1] - first[l]) + 1;
        if (first[m] < x) {
            l = m;
        } else {
            r = m;
        }
    }
    if (l == r || r == sz || first[r] - x >= x - first[l]) {
        first + l;
    }
    return first + r;
}

class TestSearch {
public:
    static void testSearching() {
        vector<int> testArr = {1, 2, 2, 3, 6, 8, 11, 12, 244};
        {
            int expectedResult = 8;
            int result = *bin_search(&testArr[0], &testArr[testArr.size() - 1], 9);
            assert(expectedResult == result);
            cout << "bin_search passed tests\n";
        }
        {
            int expectedResult = 8;
            int result = *inter_search(&testArr[0], &testArr[testArr.size() - 1], 7);
            assert(expectedResult == result);
            cout << "inter_search passed tests\n";
        }
    }
};