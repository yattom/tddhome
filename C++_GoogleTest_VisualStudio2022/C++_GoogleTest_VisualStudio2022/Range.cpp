#include "pch.h"
#include "Range.h"

Range::Range(int lower, int upper) : lower(lower), upper(upper)
{
	if (lower > upper) {
		throw std::invalid_argument("lower must be less than upper");
	}
}

int Range::getLower()
{
	return this->lower;
}

int Range::getUpper()
{
	return this->upper;
}

std::string Range::toString()
{
	return "[" + std::to_string(this->lower) + "," + std::to_string(this->upper) + "]";
}

bool Range::contains(Range other)
{
	return (lower <= other.lower && other.lower <= upper) && (lower <= other.upper && other.upper <= upper);
}
