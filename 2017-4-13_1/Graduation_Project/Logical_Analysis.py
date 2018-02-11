from snownlp import SnowNLP

def analyze(sentence) :
    s=SnowNLP(sentence)
    if(round(s.sentiments)>=0.5):
        return (round(round(s.sentiments*10)))
    else:
        return (round(round(s.sentiments*10)*(-2)))
