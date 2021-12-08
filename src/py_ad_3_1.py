"""
Chapter 3
Python Advanced(3) - Meta Class(1)
Keyword - Class of Class, Type, Meta Class, Custom Meta Class

"""
"""

메타클래스
1. 클래스를 만드는 역할 -> 의도하는 방향으로 클래스 커스텀
2. 프레임워크 작성 시 필수
3. 동적 생성(type함수), 커스텀 생성(type상속)
4. 커스텀 클래스 -> 검증클래스 등
5. 엄격한 Class 사용 요구, 메소드 오버라이드 요구

"""

'''```
# Ex1
# type 예제
# TODO
#  type => java 의 Object ? 는 아님.
#  class a:, class a(): => class a(object) 동일
# - 상속이 아니라, 원형이라는 의미라는데 잘 감은 안옴.
# - 모든 클래스의 메타 클래스는 type metaclass
#   => 언어 설계상의 정의

https://wikidocs.net/21056
- 클래스로 객체를 만들 듯 메타 클래스로 클래스를 만들 수 있다는 의미
- 클래스 선언을 동적으로 할 수 있음
- 동적으로 클래서에 멤버/함수를 추가
  - java 처럼 class 가 고정이 아니라는 생각이 필요

https://wikidocs.net/89
- 여러가지 특수 메소드
'''


class SampleA():  # Class == Object
    pass


obj1 = SampleA()  # 변수에 할당, 복사 가능, 새로운 속성, 함수의 인자로 넘기기 가능

# obj1 -> SampleA instance
# SampleA -> type metaclass
# type -> type metaclass
print('Ex1 > ', type(SampleA))
print('Ex1 > ', obj1.__class__)
print('Ex1 > ', type(obj1))
print('Ex1 > ', obj1.__class__.__class__)
print('Ex1 > ', obj1.__class__ is type(obj1))
print('Ex1 > ', type.__class__)
print('Ex1 > ', type.__mro__)
print()

# Ex2
# type meta (Ex1 증명)
# int, dict 선언
n = 10
d = {'a': 10, 'b': 20}


class SampleB:
    pass


obj2 = SampleB()

for o in (n, d, obj2):
    print('Ex2 >  {} {} {}'.format(type(o), type(o) is o.__class__, o.__class__.__class__))

print()

# the type of any new-style class is type.
print(type(SampleA))
print(type(obj2))

print()

for t in int, float, dict, list, tuple:
    print('Ex2 > ', type(t))

print('Ex2 > ', type(type))
