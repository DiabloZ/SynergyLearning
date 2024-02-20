cmake_minimum_required(VERSION 3.27)
project(__1)

set(CMAKE_CXX_STANDARD 17)

add_executable(__1 main.cpp
        TestSorting.cpp
        TestSorting.h
        TestSearch.h
        TestRecursive.h
)
