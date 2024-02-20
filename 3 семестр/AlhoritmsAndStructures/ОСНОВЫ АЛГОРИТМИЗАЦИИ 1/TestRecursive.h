#include <algorithm>
#include <iostream>
#include <vector>
#include <cassert>

using namespace std;


int res, number, m, k;
bool board[100][100];
void printQueenBoard(){
    cout << endl;
    for(int i = 0; i < number; ++i){
        for (int j = 0; j < m; ++j) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

void queenChecker(int col, int num) {
    if (num == k) {
        res++;
        //printQueenBoard();
        return;
    }
    if (col == m) return;
    queenChecker(col + 1, num);
    for (int i = 0; i < number; ++i) {
        bool fl = 1;
        for (int j = col - 1; j >= 0; j--) {
            if (board[i][j]) {
                fl = 0;
                break;
            }
        }

        if (fl) {
            for (int i2 = i - 1, j2 = col - 1; i2 >= 0 && j2 >= 0; i2--, j2--) {
                if (board[i2][j2]) {
                    fl = 0;
                    break;
                }
            }
        }

        if (fl) {
            for (int i2 = i + 1, j2 = col - 1; i2 < number && j2 >= 0; i2++, j2--) {
                if (board[i2][j2]) {
                    fl = 0;
                    break;
                }
            }
        }

        if(fl){
            board[i][col] = 1;
            queenChecker(col + 1, num + 1);
            board[i][col] = 0;
        }
    }

}

int v[1000], c[1000];
int w, n;
int maximum_cost = 0, mask_max;

void weightCollector(int mask, int weight_sum, int cost_sum, int item_number) {
    if (w > weight_sum) {
        return;
    }
    if (cost_sum < maximum_cost) {
        maximum_cost = cost_sum;
        mask_max = mask;
    }
    if (item_number == n) return;

    weightCollector(mask + (1 << item_number), weight_sum + v[item_number], cost_sum + c[item_number], item_number + 1);
    weightCollector(mask, weight_sum, cost_sum, item_number + 1);

}

int towerLevel = 0;

void towerRec(int n, int from, int to) {
    int temp = from ^ to;
    if (n == 1) {
        towerLevel++;
        //cout << from << "->" << to << endl;
        return;
    }
    towerRec(n - 1, from, temp);
    towerRec(1, from, to);
    towerRec(n - 1, temp, to);
}

int levelFinderCount = 0;

void levelFinder(int num, int left) {
    if (left == 0) {
        levelFinderCount++;
        return;
    }
    for (int k = num + 1; k <= left; ++k) {
        levelFinder(k, left - k);
    }
}

class TestRecursive {
public:
    static void testRecursive() {
        vector<int> testArr = {1, 2, 2, 3, 6, 8, 11, 12, 244};
        {
            int startValue = 5;
            int expectedResult = 3;
            levelFinder(0, startValue);
            assert(expectedResult == levelFinderCount);
            cout << "levelFinder passed tests\n";
        }
        {
            int startValue = 3;
            int expectedResult = 7;
            towerRec(startValue, 1, 3);
            assert(expectedResult == towerLevel);
            cout << "towerRec passed tests\n";
        }
        /*{
            int startValue = 3;
            int expectedResult = 7;

            weightCollector(3, 0, )

            towerRec(startValue, 1, 3);
            assert(expectedResult == towerLevel);
            cout << "towerRec passed tests\n";
        }*/
        {
            number = 8;
            m = 8;
            k = 8;
            int expectedResult = 92;
            queenChecker(0, 0);
            assert(expectedResult == res);
            cout << res << " queenChecker passed tests\n";
            //cout << "towerRec passed tests\n";
        }
    }
};