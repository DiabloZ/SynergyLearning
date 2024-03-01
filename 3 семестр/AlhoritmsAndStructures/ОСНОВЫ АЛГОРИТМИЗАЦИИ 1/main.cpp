#include "TestSorting.h"
#include "TestSearch.h"
#include "TestRecursive.h"
#include "TestOtherAlgorithms.h"

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
    TestSorting sorting;
    TestSearch search;
    TestRecursive recursive;
    TestOtherAlgorithms otherAlgorithms;
    otherAlgorithms.test();
    //sorting.testSorting();
    //search.testSearching();
    //recursive.testRecursive();
}


