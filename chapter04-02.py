# Chapter04-2
# 파이썬 반복문
# FOR 실습

# 코딩의 핵심 
# for i in <collection>
#     <loop body>

for v1 in range(10):
    print("v1 is :", v1)

print()

for v2 in range(1, 11):
    print("v2 is :", v2)

print()

for v3 in range(1, 11, 2):
    print("v3 is :", v3)

print()

# 1 부터 1000합

sum1 = 0

for v in range(1, 1001):
    sum1 += v  # sum1 = sum1 + v
print('1 ~ 1000 Sum :' , sum1)

print('1 ~ 1000 Sum :' , sum(range(1, 1001)))

print(type(range(1, 11)))

print('1 ~ 1000 4의 배수의 합 :' , sum(range(4, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플 , 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제 1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in names:
    print('You are :' , n)

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number : ", n )

# 예제 3

word = "Beautiful"

for s in word :
    print('word : ', s)

# 예제4
my_info = {
    "name": 'Lee',
    "Age" :33,
    "City": "Seoul"
}

for key in my_info:
    print('key:', my_info[key])

for v in my_info.values():
    print('value:', v )

# 예제5

name = 'FimeAppLE'
for i in name:
    if i.isupper() :
        print(i)
    else:
        print(i.upper())

# break

number = [14, 3, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for n in number:
    if n == 34:
        print('Found: 34!')
        break
    else:
        print('Not found :', n) 