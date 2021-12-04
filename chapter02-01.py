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

# %s
print('%10s' % ('nice'))
print('{:>10}' .format('nice'))

print('%-10s' % ('nice'))
print('{:10}' .format('nice'))


print('{:^10}' .format('nice'))

print('%5s' % ('nice'))
print('%.5s' % ('nicepyton')) #.은 절삭을 의미. 원래는  niceptyhon 다들어와야하는데 nicep 5글자만 들어온거 확인할 수 있디.
print('{:10.5}' .format('pythonstudy'))

# %d

print('%d %d'  % (1,2) )
print('{} {}' .format(1,2))

print('%4d'% (423434))
print('{:4d}'  .format(42))


# %f

print('%1.8f' % (3.141332434))
print('{:f}'. format(3.14134343))


print('%06.2f' % (3.1432234234))
print('{:06.2f}' .format(3.1432234234))