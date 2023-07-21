#pragma once

#include <string>

class Range
{
private:
	int lower;
	int upper;

public:
	Range(int lower, int upper);

	int getLower();
	int getUpper();
	std::string toString();
	bool contains(Range other);
};

class RangeBuilder {
private:
	int m_lower;
	int m_upper; 

public:
	RangeBuilder() : m_lower(0), m_upper(0)
	{

	}

	RangeBuilder& lower(int lower)
	{
		this->m_lower = lower;
		return *this;
	}

	RangeBuilder& upper(int upper)
	{
		this->m_upper = upper;
		return *this;
	}

	Range build()
	{
		return Range(m_lower, m_upper);
	}
};

