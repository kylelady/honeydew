#include <iostream>
#include <cstdlib>

#include "p1.h"

unsigned int fib(unsigned int n) {
	if (n == 0) {
		return 0;
	}
	if (n == 1) {
		return 1;
	}
	return fib(n - 1) + fib(n - 2);
}

int main(const int argc, const char * const * const argv) {
	unsigned int n;

	if (argc > 1) {
		n = atoi(argv[1]);
	} else {
		std::cin >> n;
	}

	unsigned int ans = fib(n);
	std::cout << ans << std::endl;

	return 0;
}
