# Chapter02-1
# 파이썬 기초과정
# print 사용법

#기본출력
print('Python start!')
print("Python start!!")
print('''Python start!''')
print("""Python start!""")

print()

# separator 옵션

print('P','Y','T','H','O','N', sep='') 
print('010','7777','1234', sep='-')
print('python','google.com',sep='@')


# end 옵션 

print('Welcome to' , end=' ')
print('IT News', end=' ')
print('Web Site')


# file 옵션
import sys

print('Learn Python', file=sys.stdout)
print()


# format 사용(d(정수)  :3 , s(문자열): 'python' , f(실수):3.14)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one', 'two'))