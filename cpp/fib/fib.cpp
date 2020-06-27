#include <chrono>
#include <cstdio>
#include <iostream>


namespace {
    int const limit = 93;
    unsigned long long int cache[limit + 1] = {0};
}

unsigned long long int fib(int n) {
    /* Read from cache */
    if (cache[n] != 0) {
        return cache[n];
    }

    /* Recursive condition */
    unsigned long long int result{0};
    if (n == 1) {
        result = 1;
    } else if (n == 0) {
        result = 0;
    } else {
        result = fib(n - 1) + fib(n - 2);
    }

    /* Update cache */
    cache[n] = result;
    return result;
}

int main() {
    int n;
    while (true) {
        /* Receive input from terminal */
        std::cout << "Please input integer not over " << limit << std::endl;
        scanf("%d", &n);
        if (n > limit || n < 0) {
            printf("Incorrect input\n");
            continue;
        }

        /* Start execute timestamp */
        auto start = std::chrono::high_resolution_clock::now();

        auto result = fib(n);
        std::cout << "Fibonacci number " << n << " is : " << result << std::endl;

        /* Stop execute timestamp */
        auto stop = std::chrono::high_resolution_clock::now();
        /* Total execute time */
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
        std::cout << "Process time is : " << duration.count() << " microseconds\n" << std::endl;
    }
}