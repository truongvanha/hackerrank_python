if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, raw_input().strip().split()))
    z = max(arr)
    while max(arr) == z:
        arr.remove(max(arr))
    print(max(arr))
