def add(n):
    if n == 1:
        return 1
    else:
        return n + add(n-1)

def main():
    print(add(10))

main()
