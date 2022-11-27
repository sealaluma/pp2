import json
with open('movies.json') as f:
    data = f.read()
js = json.loads(data)


def average(movies): 
    avg = 0
    numM = len(js)
    for di in js:
        avg = avg + di['imdb']
    avg = avg / numM
    return avg

avrg = average(js)
print(avrg)