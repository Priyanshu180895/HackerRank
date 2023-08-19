def sockMerchant(n, ar):
    pair_count = []
    for i in set(ar):
        pair_count.append(ar.count(i))
    return sum(i//2 for i in pair_count)


if __name__ == "__main__":
    n = int(input("Enter size of list: ").strip())
    ar = list(map(int,input("Enter elements of array: ").rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)