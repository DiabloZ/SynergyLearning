#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

template<class T>
void sort_chose(vector<T> &v) {
    vector<T> res;
    size_t sz = v.size();
    vector<bool> p(sz, false);
    for (int i = 0; i < sz; ++i) {
        T mi;
        bool fl = false;
        size_t num = 0;
        for (int j = 0; j < sz; ++j) {
            if (!p[j] && (!fl || mi > v[j])) {
                mi = v[j];
                num = j;
                fl = true;
            }
        }
        p[num] = true;
        res.push_back(mi);
    }
    v = res;
}


template<class T>
void merge_sort(vector<T> &v, size_t l, size_t r) {
    if (l == r) return;
    size_t m = (l + r) / 2;
    merge_sort(v, l, m);
    merge_sort(v, m + 1, r);
    vector<T> merged (r - l + 1);
    merge(v.begin() + l, v.begin() + m + 1, v.begin() + m + 1, v.begin() + r + 1, merged.begin());
    copy(merged.begin(), merged.end(), v.begin() + l);
}

template<class T>
void sort_merge(vector<T> &v) {
    merge_sort(v, 0, v.size() - 1);
}

class TestSorting {
public:
    static void testSorting() {
        vector<float> _v1 = {3, 1, 2, 1, 5, 4};
        vector<int> _v2 = {5, 6, 1, -1, 100, -100, 2, 500, 0};
        vector<int> _v3 = {0};
        vector<float> expected_v1 = {1, 1, 2, 3, 4, 5};
        vector<int> expected_v2 = {-100, -1, 0, 1, 2, 5, 6, 100, 500};
        vector<int> expected_v3 = {0};
        {
            vector<float> v1 = _v1;
            vector<int> v2 = _v2;
            vector<int> v3 = _v3;
            sort_chose(v1);
            sort_chose(v2);
            sort_chose(v3);
            assert(v1 == expected_v1);
            assert(v2 == expected_v2);
            assert(v3 == expected_v3);
            cout << "Chose passed tests\n";
        }
        {
            vector<float> v1 = _v1;
            vector<int> v2 = _v2;
            vector<int> v3 = _v3;
            sort_merge(v1);
            sort_merge(v2);
            sort_merge(v3);
            assert(v1 == expected_v1);
            assert(v2 == expected_v2);
            assert(v3 == expected_v3);
            cout << "Merge passed tests\n";
        }
    }
};