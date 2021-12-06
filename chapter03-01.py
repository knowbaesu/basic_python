# Chapter03-01
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린(논리)
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = 'Anavonda'
float_s = 10.0 # 10 == 10.0
int_s = 7
list = [str1,str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = (7,8,9) # tuple = 7,8,9 이것도 상관없음
set = {7,8,9}

# 데이터 타입 출력

print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_s))
print(type(int_s))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
// : 목
% : 나머지
abs(x) : 절대값
pow(x,y), x**y : x에 y제곱
"""

# 정수 선언
i = 77
i2 = -14
big_int = 7777777777777777777777777777799999999


# 정수 출력
print(i)
print(i2)
print(big_int)

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()


# 연산 실습
i1= 39
i2 = 939
big_int1 = 9999999999999999999
big_int2 = 9999999999999999999
f1 = 7.888
f2 = 3.999
# +
print(">>>>+")
print("i1 + i2 :", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)

print(">>>>*")
print("i1 * i2 :", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)


# 형 변환 실습
a = 3. #0 생략가능
b = 6
c = .7 #마찬가지로 0 생략가능
d = 12.7


# 타입 출력
print(type(a)),print(type(b)) , print(type(c)), print(type(d))

# 형변환 
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # Ture는 1 False는 0
print(float(False))
print(complex(3))
print(complex('3')) #문자형 -> 숫자형으로
print(complex(False))



# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y)

print(pow(5,4), 5**4)


# 외부 모듈
import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi)

