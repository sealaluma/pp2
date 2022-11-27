import json
with open('movies.json') as f:
    data = f.read()
js = json.loads(data)

ml = []
category = input()
def good_quality(category, js):
    for di in js:
        if di["category"] == category:
            ml.append(di["name"])
            
good_quality(category, js)
print(ml)

def average(movies): 
    avg = 0
    numM = len(ml)
    for di in js:
        avg = avg + di['imdb']
    avg = avg / numM
    return avg
avrg = average(js)
print(avrg)
