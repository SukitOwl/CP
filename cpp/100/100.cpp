#include <cstdio>

int three_n_plus_1(int n, int (&cache)[1000000])
{
    int result = 0;
    if (n < 1000000) {
        if (cache[n] > 0) {
            return cache[n];
        }
    }
    if (n > 1)
    {
        int next_n = 0;
        if (n % 2 == 1)
        {
            next_n = (3 * n) + 1;
        }
        else
        {
            next_n = n / 2;
        }
        result = three_n_plus_1(next_n, cache);
    }
    if (n < 1000000) {
        cache[n] = result + 1;
    }
    return result + 1;
}


int main()
{
    int cache[1000000] = {0};
    int i, j;
    while (scanf("%d%d", &i, &j) != EOF)
    {
        int x = 0, y = 0, k = 0, max = 0;
        x = (i > j) ? i : j;
        y = (i < j) ? i : j;
        for (k = x; k >= y; k--)
        {
            if (cache[k] != 0)
            {
                if (cache[k] > max) {
                    max = cache[k];
                }
            }
            else
            {
                int length = three_n_plus_1(k, cache);
                if (length > max)
                {
                    max = length;
                }
            }
        }
        printf("%d %d %d\n", i, j, max);
    }
    return 0;
}