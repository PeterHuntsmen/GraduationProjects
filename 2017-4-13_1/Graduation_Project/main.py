# encoding='utf-8'

from Graduation_Project.participle import *
from Graduation_Project.Logical_Analysis import analyze
from Graduation_Project.POS_Tagging import POS_Tagging
from Graduation_Project.keywords import summary

route = "E:/Test/test_4.txt"
text = open(route).read()
temp = division(route)
result = analyze(temp)
buffer = POS_Tagging(route)
summary = summary(route)
print("本文本倾向性为：")
print(result)
print("本文主旨为：")
print(summary)
