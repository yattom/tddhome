#pragma once

extern int mul2(int v);

class Counter {
private:
	int _value;

public:
	Counter();
	int value();
	void up();
};