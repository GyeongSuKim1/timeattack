# 시리얼라이즈를 임포트 해줌
from pyexpat import model
from re import A
from statistics import mode
from rest_framework import serializers





'''
메타 클래스가 시리얼라이즈 에서 제일 중요 함
    user serializers 에선 모델, 필드 두 가지가 가장 중요 함

UserSerializer 에서 model과 fields 를 지정을 해줘서 model안에 있는 데이터 중 
fields 로 적은 데이터들을 json 형식으로 return 해줌 
'''

