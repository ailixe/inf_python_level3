"""
Chapter 1
Python Advanced(1) - Python Variable Scope
Keyword - scope, global, nonlocal, locals, globals..

"""
"""
              global     local
함수안읽기       0          0
함수안쓰기       X*         0  
함수밖읽기       0          X
함수밖쓰기       0          X

# 전역변수
1. 주로 변하지 않는 고정 값에 사용

# 지역변수
1. 지역변수는 함수 내에 로직 해결에 국한
  - 소멸주기 함수 실행 해제 시
2. 전역변수를 지역내에서 수정되는 것은 권장X

## newinx
코딩시 사용
- global
- nonlocal

정보 조회
- locals()
- globals()

"""
################# Ex1
a = None
print(a is not None and len(a) > 0)

a = 10  # Global variable


def foo():
    # Read global variable
    print('Ex1 > ', a)


foo()
# Read global variable
print('Ex1 > ', a)
print()

################# Ex2
b = 20


def bar():
    b = 30  # Local variable
    print('Ex2 > ', b)  # Read local variable


bar()

print('Ex2 > ', b)  # Read global variable
print()
# <= 여긴 얼마가 나올까요 ? by 상근님

################# Ex3
c = 40


def foobar():
    # c = c + 10   # UnboundLocalError
    # c = 10
    # c += 100

    print('Ex3 > ', c)


foobar()
print()

# 이게 java 와는 다른 부분인듯

################# Ex4
d = 50


def barfoo():
    # 전역 변수가 선언되어 있어도, local 에서 사용하려면 바로 사용은 불가능
    global d
    d = 60
    print('Ex4 > ', d)


barfoo()

print('Ex4 > ', d)  # Prints 5. Global variable d was modified within barfoo()
print()


################# Ex5(중요) !!!
def outer():
    e = 70

    def inner():
        nonlocal e
        e += 10  # e = e + 10
        print('Ex5 > ', e)

    return inner


in_test = outer()  # Closure

print(in_test)

in_test()
in_test()
print()

# 다시보는 1급객체
# - 함수의 인자로 전달되거나,
# - 함수의 반환값이 되거나,
# - 수정되고 할당되는 것들을 전제로 한다.
# ex) list, str, int 등등

################# Ex6
import pprint as pp


def func(var):
    x = 10

    def printer():
        print('Ex6 > ', "Printer Func Inner")

    print('Ex6 > Func Inner', locals())  # 지역 전체 출력
    print("## pprint")
    pp.pprint(locals())
    print()


func("Hi")

################# Ex7
print('Ex7 >')
print(globals())  # 전역 전체 출력
pp.pprint(globals())
print()

# 1 처럼 쓰면, 2 처럼 해석되어 실행
# 1
# test_variable = 100
# 2
globals()['test_variable'] = 100
print('Ex7 >')
print(globals())
pp.pprint(globals())
print()

################# Ex8(지역 -> 전역 변수 작성)
# 동적으로 변수를 생성할 수도 있다.
for i in range(1, 10):
    for k in range(1, 10):
        globals()['plus_{}_{}'.format(i, k)] = i + k

print("EX8 >")
print(plus_3_5)
print(plus_9_9)
pp.pprint(globals())

exit()
