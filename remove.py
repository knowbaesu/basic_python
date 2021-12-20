max_01 = 0
min_01 = 0
def myMean(a):
    for i in a:
        if i > max_01:
            max_01 = i
        if i < min_01:
            min_01 = i
    a.remove(max_01)
    a.remove(min_01)
    return print(sum(a)/len(a))
myMean([1,2,3,4,5])


p = 0
count = int(input())
s = []
while True :
    order = input()
    for i in order:
        if i =='아메리카노':
            s.append(4100)
        elif i == '카페라떼':
            s.append(4600)
        elif i == '카라멜마끼아또':
            s.append(5100)
    p =p+1
    if count == p:
        break
print(s)