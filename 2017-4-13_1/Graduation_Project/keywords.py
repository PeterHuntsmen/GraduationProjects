from snownlp import SnowNLP

def summary(route):
    file = open(route)
    text = file.read()
    s = SnowNLP(text)
    words = s.summary(1)
    result = str(words).replace("'","").replace("[","").replace("]","")
    return result

def keywords(route):
    file = open(route)
    text = file.read()
    s = SnowNLP(text)
    keywords = s.keywords(1)
    result = str(keywords).replace("'","").replace("[","").replace("]","")
    return result