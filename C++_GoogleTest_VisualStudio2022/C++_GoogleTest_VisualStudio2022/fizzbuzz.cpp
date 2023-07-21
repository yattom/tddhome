#include "pch.h"
#include "fizzbuzz.h"

std::string fizzbuzz(const int num)
{
    if (num % 3 == 0) {
        return "Fizz";
    }
    return std::to_string(num);
}



