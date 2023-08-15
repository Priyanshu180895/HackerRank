def mars_exploration(s):
    altered_count = 0
    expected = "SOS"

    for i in range(len(s)):
        if s[i] != expected[i%3]:
            altered_count += 1
    return altered_count

s = input("Enter the received message: ").strip()
altered_count = mars_exploration(s)
print(altered_count)

