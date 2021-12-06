# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성

str1 = "I am Python"
str2 = 'Python'
str3 ="""How are you doing?"""
str4 = '''Thank you!'''


print(type(str1),type(str2),type(str3),type(str4))
print(len(str1),len(str2),len(str3),len(str4))  #len 공백포함

# 빈 문자열
str_t1 = '' #""도 가능
str_t2 = str() 

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자 사용
# I'm Boy 

print("I'm boy")