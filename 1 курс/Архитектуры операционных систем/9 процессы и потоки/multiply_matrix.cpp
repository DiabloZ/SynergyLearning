#include <unistd.h>
#include <string>
#include <cstring>
#include <stdio.h>
#include <sys/wait.h>


using namespace std;

int makeOtherProcess() {

    const int maxSizeOfArray = 2;
    int matrixA [maxSizeOfArray][maxSizeOfArray] = {
            {3,5},
            {2, 1},
    };

    int matrixB [maxSizeOfArray][maxSizeOfArray] = {
            {8, 2},
            {1, 7},
    };

    int resultArray[maxSizeOfArray][maxSizeOfArray];
    memset(resultArray, 0, sizeof(resultArray));


    int fd1[2];
    int fd2[2];
    char input_str[100];
    pid_t  p;


    if(pipe(fd1) == -1 || pipe(fd2) == -1 ){
        fprintf(stderr, "Pipe Failed");
    }

    p = fork();

    if(p < 0) {
        fprintf(stderr, "Fork Failed");
        return 1;
    } else if (p > 0) {
        char concat_str[1000];
        close(fd1[0]);
        write(fd1[1], input_str, strlen(input_str) + 1);
        close(fd1[1]);
        wait(NULL);

        close(fd2[1]);
        read(fd2[0], concat_str, 1000);
        printf("%s","Результат - \n");
        printf("%s\n", concat_str);
        close(fd2[0]);
    } else {
        close(fd1[1]);
        char concat_str[100];
        read(fd1[0], concat_str, 100);

        for (int i = 0; i < maxSizeOfArray; ++i){
            for(int j = 0; j < maxSizeOfArray; ++j){
                for(int k = 0; k < maxSizeOfArray; ++k){
                    resultArray[i][j] +=  matrixA[i][k] * matrixB[k][j];
                }
            }
        }

        for (int i = 0; i < maxSizeOfArray; i++){
            for(int j = 0; j < maxSizeOfArray; j++){
                if (j == 0){
                    std::string s = std::to_string(i + 1);
                    char const *pchar = s.c_str();
                    strcat(concat_str, pchar);
                    strcat(concat_str, "- ");
                }
                char integer_string[3];
                sprintf(integer_string, "%d", resultArray[i][j]);
                strcat(concat_str, integer_string);

                if (j == 0){
                    strcat(concat_str, ", ");
                }
            }
            strcat(concat_str, "\n");
        }

        close(fd1[0]);
        close(fd2[0]);
        write(fd2[1], concat_str, strlen(concat_str) + 1);
        close(fd2[1]);
    }
}

int main() {
    setlocale(LC_ALL, "RU");
    makeOtherProcess();
	return 0;
}



