import pickle

with open('banner.p','rb') as f:
    data = pickle.load(f)
for outer in data:
    for tup in outer:
        print(tup[0]*tup[1],end="")
    print()

#answer = channel
