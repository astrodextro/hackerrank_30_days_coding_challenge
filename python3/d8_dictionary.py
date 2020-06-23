
def performSearch(pb, keyword):
    if keyword in pb:
        print("{}={}".format(keyword, pb[keyword]))
    else:
        print("Not found")

t = int(input())
if __name__ == '__main__':
    phoneBook = dict()
    for i in range(0, t):
        arr = input().rstrip().split()
        if len(arr) != 2:
            exit("Input must contain only two values")
        phoneBook[arr[0]] = arr[1]
    while True:
        try:
            performSearch(phoneBook, input())
        except EOFError:
            exit()