"""
Chapter 4
Python Advanced(4) - 나만의 패키지 만들기(3) - PyPI 배포
Keyword - PyPI, build, package deploy

"""

# py_ad_4_3 : 완성된 패키지 임포트
from py_ad_4_3 import GifConverter as gfc

# 클래스 생성
c = gfc("./project/images/*.png", './project/image_out/result.gif', (500, 240))

# 실행
c.convert_gif()

"""

패키지 배포 순서(PyPI)
1. https://pypi.org/ 회원가입
2. 프로젝트 구조 확인
3. __init__.py 생성
  - 패키지로 인식함
4. 프로젝트 Root 필수 파일 작성
- .gitignore
  - pip install github 를 이용해서 설치도 가능
- LICENSE
  - 오픈소스 라이센스. MIT
  - https://opensource.org/licenses/MIT
- MANIFEST.in
  - pytnon 파일외에도 포함되어야 하는 파일들을 기술
- README.md
- setup.py
  - pypi 에 나오는 정보
- setup.cfg(optional)

5. pip install setuptools wheel 설치 후 빌드업 -> 설치판 생성
-> 설치1 : python -m pip install  --upgrade setuptools wheel 
-> 설치2 : python -m pip install  --user --upgrade setuptools wheel
-> 빌드 : python setup.py sdist bdist_wheel
- wheel
  - 실행파일 형식으로 만들어줌
- setuptools
  - 압축

6. PyPI 배포
-> 설치 : pip install twine
-> 업로드 : python -m twine upload dist/*

7. 설치 확인(pip install pygifconvt)
- > from pygifconvt import GifConverter as Alias

"""
