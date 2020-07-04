#Write your code here
class Calculator():
    def power(self, n: int, a: int):
        if n < 0 or a < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n**a

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e) 