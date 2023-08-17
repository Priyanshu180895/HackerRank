def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

s = input("Enter 1st String: ")
t = input("Enter 2nd String: ")
print(strings_xor(s, t))