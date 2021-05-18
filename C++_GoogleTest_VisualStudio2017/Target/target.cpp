#include "stdafx.h"
#include "target.h"

int mul2(int v) {
	return v * 2;
}


Counter::Counter() {
	_value = 0;
}

int Counter::value() {
	return _value;
}


void Counter::up() {
	_value += 1;
}
