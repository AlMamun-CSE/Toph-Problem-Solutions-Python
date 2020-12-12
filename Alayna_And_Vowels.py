def check_vowels(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            count += 1
    return count


s = input().lower()
print(check_vowels(s))
