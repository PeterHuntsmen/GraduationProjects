#encoding='utf-8'
import jieba
import jieba.posseg
def division (route):
    final_word = ""
    file = open(route.encode('utf-8'))
    for text in file.readlines():
        temp = jieba.cut(text, cut_all=False)
        result = "/".join(temp)
        final_word+= result
    return final_word
    file.close()