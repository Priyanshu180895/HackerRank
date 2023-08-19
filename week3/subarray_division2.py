def birthdays(s,d,m):
    i = 0
    j = m
    count = 0

    while j <= len(s):
        if sum(s[i:j]) == d:
            count += 1
        i += 1
        j += 1
    return count

if __name__ == "__main__":
    n = int(input("No. of elements in a array: ").strip())
    s = list(map(int,input("Enter elements of array: ").rstrip().split()))

    birthday_days_month = input("Enter b'day day and month: ").rstrip().split()

    d = int(birthday_days_month[0])
    m = int(birthday_days_month[1])

    result = birthdays(s, d,m)

    print(result)   