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

print("I'm Boy")
print("I\'m Boy")
print('a \t b')
print('a \"\" b')

escape_str1= "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈

t_s1 = "Click \t start!"  #탭
t_s2 = "New Line \n Check!" # 줄바꿈

print(t_s1) 
print(t_s2)
print()


# Raw String  

raw_s1 = r'D:\pyton\test'
print(raw_s1)

# 멀티라인 입력 (내용이 길때)

# multi_str = "asddddddddddsaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"

# 멀티라인 입력
#따옴포를 밑으로 내리면 오류가 난다

multi_str ='''  
String
Multi line
Test
'''

multi_str2 = \
"""
String
Multi ine
Test
"""

# \를 앞에 배치해 줬을 경우 밑으로 내려도 아무 이상이 없는걸 볼 수 있다.

print(multi_str)
print(multi_str2)

# 다른줄에 썼는데도 붙여서 나온다.
cu = \
'asd' \
'aaa'\
'bbb'\

print(cu)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startwith, count, edswith, isalpha...)

print("Capitalize:", str_o1.capitalize()) #capitalize(첫글자 대문자 만들기)
print("endswith:", str_o2.endswith("e")) # 끝글자 체크
print("replace:", str_o1.replace("thon", 'Good')) #찾아 바꾸기
print("sorted:", sorted(str_o1))
print("split:", str_o4.split(' '))

# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str)) #__iter__

# 출력
for i in im_str:
    print(im_str)