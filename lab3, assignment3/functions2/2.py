import json
with open('movies.json') as f:
    data = f.read()
js = json.loads(data)


ml = []
def good_quality(js):
    for di in js:
        if di["imdb"] > 5.5:
            ml.append(di["name"])
good_quality(js)
print(ml)