#encoding='utf-8'

import jieba
import jieba.posseg

def POS_Tagging(route):
    final_word=""
    lines = open(route).readlines()
    for line in lines:
        words = jieba.posseg.cut(line)
        for w in words:
            final_word = final_word + w.word + w.flag + " "
    return final_word