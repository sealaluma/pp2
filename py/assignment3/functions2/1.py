import json
with open('movies.json') as file:
    data = file.read()
js = json.loads(data)

movie = input()
def good_quality(movie, js):
    for di in js:
        if di["name"] == movie and di["imdb"] > 5.5:
            return True
    return False
print(good_quality(movie, js))