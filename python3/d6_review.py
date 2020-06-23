def decoration(func):
    def wrapper(stringInput):
        stri = func(stringInput)
        print(stri)
    return wrapper

@decoration
def decomposeString(stringInput):
    chars = list(stringInput)
    evenChars = []
    oddChars = []
    for i in range(0, len(chars)):
        if i % 2 == 0: #even
            evenChars.append(chars[i])
        else: #odd
            oddChars.append(chars[i])

    return "".join(evenChars) + " " + "".join(oddChars)

t = int(input())
if __name__ == '__main__':
    strings = []
    for i in range(0, t):
        strings.append(input())
    
    for i in range(0, t):
        decomposeString(strings[i])
