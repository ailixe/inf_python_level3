"""
Chapter 2
Python Advanced(2) - Property(1) - Underscore
Keyword - access modifier(접근지정자), underscore
"""
"""
다양한 언더스코어 활용
파이썬 접근지정자 설명
- private, protected, public
"""

# Ex1
# Use underscore
# 1.인터프리터
# 2.값 무시
# 3.네이밍...(국제화, 자릿수 등)

# Unpacking - 값을 무시
x, _, y = (1, 2, 3)
a, *_, b = (1, 2, 3, 4, 5)
print('Ex1 >', x, y, a, b)

a, *i, b = (1, 2, 3, 4, 5)
print('Ex1 >', i)
print('Ex1 >', type(i))
# exit(0)

for _ in range(10):
    pass

for _, val in enumerate(range(10)):
    pass


# Ex2
# 접근지정자
#   name : public
#  _name : protected
# __name : private
# 파이썬 -> Public 강제 X, 약속된 규약에 따라 코딩 장려(자유도, 책임감 장려)
# - 타 클래스(클래스변수,인스턴스 변수 값 쓰기 장려 안함), -> Naming Mangling
#   - method 를 통해서 해라
# - 타 클래스 __ 접근하지 않는 것이 원칙.

# No use Property

class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0 # _SampleA_y
        self._z = 0


a = SampleA()
a.x = 1
# print(a.__y)
# a.__y = 6
# exit(0)

print('Ex2 > x : {}'.format(a.x))
# Test
# print('Ex2 > y : {}'.format(a.__y))
print('Ex2 > z : {}'.format(a._z))
# dir 로 속성 조회
print('Ex2 > dir a : ', dir(a))  # _SampleA__y
# exit(0)


# 강제성이 있는가 ?
# - 암묵적인 규약을 지키자.
# - public 한 멤버외에는 메소드를 통하는 것으로.
# a._SampleA__y = 2 # 수정 가능
# print('Ex2 > y : {}'.format(a._SampleA__y))


# Ex3
# 메소드 활용 Getter, Setter 작성

class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value


b = SampleB()

b.x = 1
b.set_y(2)

print('Ex3 > x : {}'.format(b.x))
print('Ex3 > y : {}'.format(b.get_y()))

# 변수 접근 후 수정 부분에서 일관성, 가독성 하락
print('Ex3 >', dir(b))  # _SampleB__y
