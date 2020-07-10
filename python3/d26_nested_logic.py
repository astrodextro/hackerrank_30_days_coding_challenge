curDay, curMo, curYr = list(map(int, input().strip().split(' ')))
exDay, exMo, exYr = list(map(int, input().strip().split(' ')))

amt = 0

# rd, rm, ry = [int(x) for x in input().split(' ')]
# ed, em, ey = [int(x) for x in input().split(' ')]

# if (ry, rm, rd) <= (ey, em, ed):
#     print(0)
# elif (ry, rm) == (ey, em):
#     print(15 * (rd - ed))
# elif ry == ey:
#     print(500 * (rm - em))
# else:
#     print(10000)

if exYr < curYr:
    amt = 10000
elif exYr == curYr:
    if exMo < curMo:
        amt = 500 * (curMo - exMo)
    elif exMo == curMo:
        if exDay < curDay:
            amt = 15 * (curDay - exDay)
print(amt)
