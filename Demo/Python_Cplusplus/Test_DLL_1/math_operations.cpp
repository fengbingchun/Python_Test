#include "math_operations.hpp"
#include <iostream>

FBC_EXPORTS int add_(int a, int b)
{
	fprintf(stdout, "add operation\n");
	return a + b;
}

FBC_EXPORTS int sub_(int a, int b)
{
	fprintf(stdout, "sub operation\n");
	return a - b;
}

FBC_EXPORTS int mul_(int a, int b)
{
	fprintf(stdout, "mul operation\n");
	return a * b;
}

FBC_EXPORTS int div_(int a, int b)
{
	if (b == 0) {
		fprintf(stderr, "b can't equal 0\n");
		return -1;
	}

	return (a / b);
}

