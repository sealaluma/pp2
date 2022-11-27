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