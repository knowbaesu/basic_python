# Chapter 03-05
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용 (Json)
# 딕져너리 자료형(순서x, 키 중복X, 수정o, 삭제o)


# 선언
a = {'name':'Kim', 'phone': "010-888-0777", 'birth' : '971022'}
b = {0 : 'Heollo Python'}
c = {'arr': [1,2,3,4]}
d = {
    'Name' : 'nusin',
    'City' : 'Busan',
    'Age'  : 33,
    'Grade' : 'A',
    'Status' : True
}
 
e = dict([
    ( 'Name' , 'nusin'),
    ('City' , 'Busan'),
    ('Age', 33),
    ('Grade', 'A'),

    ('Status', True)
])

f = dict(
    Name ='Good',
    City = 'Busan',
    Age = 49,
    Grade = 'A',
    Status = True
)


# a = [f1, f2, f3...]


print('a - ',  type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 츌력
print('a -', a['name'])   #키가 존재하지 않으면 에러발갱
print('a -', a.get('name')) # 키가 존재하지 않으면 None 처리
print('b -', b[0])
print('b -', b.get(0))
print('f -', f.get('City'))
print('f -', f.get('Age'))