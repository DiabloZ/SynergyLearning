#include "TestSorting.h"
#include "TestSearch.h"
#include "TestRecursive.h"

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
    TestSorting test;
    TestSearch search;
    TestRecursive recursive;
    //test.testSorting();
    //search.testSearching();
    recursive.testRecursive();
}


