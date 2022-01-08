# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 23:24:18 2022

@author: Doshite368
"""

#서양어대 = []
#서양어대, 사회과학대학 있으면, 대학 소개 - > 리스트 내에 있는지 여부로
occidental = ["노어과","스페인어과","독일어과","프랑스어학부","이탈리아어과","스칸디나비아어학과","네덜란드어과","포르투갈어과"]
social_science = ["정치외교학과","행정학과","미디어커뮤니케이션학부"]

class hufs():
    def __init__(self, name, major):
        self.name = name
        self.major = major 
    def introduce1(self):
        if self.major in social_science: #이름, 학과 
            print("안녕하세요 저는 한국외대 {2} {0}에 재학중인 {1} (이)라고 합니다.".format(self.major,self.name,"사회과학대학"))
        elif self.major in occidental:
            print("안녕하세요 저는 한국외대 {2} {0}에 재학중인 {1} (이)라고 합니다.".format(self.major,self.name,"서양어대학"))
        else:
            print("안녕하세요 저는 {0}에 재학중인 {1}라고 하는데요, 저는 그냥 외대생이에요.".format(self.major,self.name)) #서대, 사대 아닐 경우 그냥 외대생으로
        


class Dualmajor(hufs):
    def introduce2(self,dualmajor): #이중전공 input 받음
        print("저는 {2}이고, {0}와 {1}를(을) 전공으로 하고 있어요.".format(self.major,dualmajor,self.name))





kwak = hufs("명곤","프랑스어학부")
park = hufs("성주","정치외교학과")
yoon = hufs("현섭","ELLT")

kwak.introduce1()
park.introduce1()
yoon.introduce1()

print("-"*10)

kwak = Dualmajor("명곤","프랑스어학부")
kwak.introduce2("중국어")

park = Dualmajor("성주","정치외교학과")
park.introduce2("경영학과")


#반성
#변수 설정 규칙 제대로 따르기 - 스스로 헷갈림
#0,1,2,3 순서로 시작됨

#질문
#self는 언제, 어떤 식으로 쓰는가