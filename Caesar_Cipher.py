def caesar_encrypt(realText, step):
    outText = []
    cryptText = []

    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

    for eachLetter in realText:
        if eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            crypting = (index - step) % 26
            cryptText.append(crypting)
            newLetter = lowercase[crypting]
            outText.append(newLetter)
        elif eachLetter == ' ':
            outText.append(' ')
    return outText


n = int(input())
s = input().lower()
code = caesar_encrypt(s, n)
output_string = ''.join(code)
print(output_string.strip())
