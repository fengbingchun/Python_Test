#include "funset.hpp"
#include <random>
#include <iostream>

PYBIND11_API int get_random_number(int min, int max)
{
    fprintf(stdout, "get random number through std::uniform_int_distribution\n");
    std::random_device rd;
    std::mt19937 generator(rd());
    std::uniform_int_distribution<int> distribution(min, max);
    return distribution(generator);
}
