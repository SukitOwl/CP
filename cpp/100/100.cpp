#include <cstdio>
#include <unordered_map>
#include <vector>


int three_n_plus_1(int n, int length, std::unordered_map<int, int> &cache, std::vector<int> &arr) 
{
    auto cache_item = cache.find(n);
    if (cache_item != cache.end()) 
    {
        length = length + cache_item->second;
        return length;
    }
    else
    {
        // arr.push_back(n);
        length = length + 1;
        if (n == 1)
        {
            return length;
        }
        else
        {
            int next_n = 0;
            if (n % 2 == 1) 
            {
                next_n = (3 * n) + 1;
            }
            else 
            {
                next_n = next_n / 2;
            }
            return three_n_plus_1(next_n, length, cache, arr);
        }
    }
}


// void update_cache(int length, std::unordered_map<int, int> &cache, std::vector<int> &arr)
// {
//     int index = -1;
//     for (int n : arr)
//     {
//         index = index + 1;
//         cache[n] = length - index;
//     }
// }


int main()
{
    std::unordered_map<int, int> cache = {};
    int i, j;
    while (scanf("%d%d", &i, &j) != EOF)
    {
        int x = 0, y = 0, k = 0, max = 0;
        x = (i > j) ? i : j;
        y = (i < j) ? i : j;
        for (k = x; k >= y; k--)
        {
            auto cache_item = cache.find(k);
            if (cache_item != cache.end()) 
            {
                if (cache_item->second > max) {
                    max = cache_item->second;
                }
            }
            else 
            {
                std::vector<int> arr = {};
                int length = three_n_plus_1(k, 0, cache, arr);
                // update_cache(length, cache, arr);
                // if (length > max)
                // {
                    // max = length;
                // }
            }
        }
        printf("%d %d %d\n", i, j, max);
    }
    return 0;
}