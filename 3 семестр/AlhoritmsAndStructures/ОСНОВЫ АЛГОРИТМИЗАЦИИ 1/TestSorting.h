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

template<class T>
void fast_sort(vector<T>& v, size_t l, size_t r);

template<class T>
void fast_sort(vector<T>& v, size_t l, size_t r) {
    if (l >= r) return;
    size_t sz = r - l + 1;
    size_t m = l + rand() % sz;
    vector<T> lb, rb, mb;
    for (size_t i = l; i <= r; ++i) {
        T& val = v[i];
        if (val < v[m]) lb.push_back(val);
        else if (val > v[m]) rb.push_back(val);
        else mb.push_back(val);
    }
    copy(lb.begin(), lb.end(), v.begin() + l);
    copy(mb.begin(), mb.end(), v.begin() + l + lb.size());
    copy(rb.begin(), rb.end(), v.begin() + l + lb.size() + mb.size());

    if (l + lb.size() > l + 1) {
        fast_sort(v, l, l + lb.size() - 1);
    }
    if (r - rb.size() + 1 < r) {
        fast_sort(v, r - rb.size() + 1, r);
    }
}

template<class T>
void sort_fast(vector<T>& v) {
    fast_sort(v, 0, v.size() - 1);
}

template<class T>
void sort_count(vector<T>& v, size_t sz) {
    vector<size_t> counters (sz * 2, 0);
    for (T& val : v) {
        counters[abs(val) + (sz - 1) * (val < 0)]++;
    }
    size_t uk = 0;
    for (size_t i = sz * 2 - 1; i >= sz; --i) {
        T val = -((int)i - (int)sz + 1);
        for (size_t j = 0; j < counters[i]; ++j) {
            v[uk] = val;
            uk++;
        }
    }
    for (size_t i = 0; i < sz; ++i) {
        T val = i;
        if (i > sz - 1) val = -(val - (int) sz + 1);
        for (size_t j = 0; j < counters[i]; ++j) {
            v[uk] = val;
            uk++;
        }
    }
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
            cout << "Chose sort passed tests\n";
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
            cout << "Merge sort passed tests\n";
        }
        {
            vector<float> v1 = _v1;
            vector<int> v2 = _v2;
            vector<int> v3 = _v3;
            sort_fast(v1);
            sort_fast(v2);
            sort_fast(v3);
            assert(v1 == expected_v1);
            assert(v2 == expected_v2);
            assert(v3 == expected_v3);
            cout << "Fast sort passed tests\n";
        }
        {
            vector<float> v1 = _v1;
            vector<int> v2 = _v2;
            vector<int> v3 = _v3;
            sort_count(v1, 100);
            sort_count(v2, 1000);
            sort_count(v3, 1000);
            assert(v1 == expected_v1);
            assert(v2 == expected_v2);
            assert(v3 == expected_v3);
            cout << "Count sort passed tests\n";
        }
    }
};