#encoding:utf-8

import jieba
import matplotlib.pyplot as plt
import os
from tkinter import *

def statistics(route):

    if os.path.exists(route):
        route_of_stopwords = "E:/Test/stopwords.txt"
        file = open(route,'r').read()
        stopWords = {}.fromkeys([line.rstrip() for line in open(route_of_stopwords, 'r')])
        segs = jieba.cut(file,cut_all=True)
        final = ''
        for seg in segs:
            if seg not in stopWords:
                final += (str(seg)+"")
        word_freq={}
        words = jieba.cut(final,cut_all=False)
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        freq_word = []
        for word, freq in word_freq.items():
            freq_word.append((word, freq))
        freq_word.sort(key=lambda x: x[1], reverse=True)
        max_number = 20
        frequency = []
        Words = []
        for word, freq in freq_word[:max_number]:
            Words.append(word)
            frequency.append(freq)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置
        plt.rcParams['axes.unicode_minus'] = False
        plt.title("对 " + route + "的词频统计：")
        plt.bar(range(len(frequency)),frequency,tick_label=Words)
        plt.show()

    else:
        root = Tk()
        root.title("Error Occurred!")
        root.geometry('%dx%d' % (300, 180))
        Label(text = "文件不存在~!").pack()
        root.mainloop()
