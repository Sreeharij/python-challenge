#the sequence proceeds in a manner where i`th number is a concatanation of continuous frequency_count and number of (i-1)`th number.
#eg 111221 3 ones plus 2 twos plus 1 one. I.e 312211

arr = [1,11,21,1211,111221]

current = str(arr[4])
def get_next(current):
    current = str(current)
    string = ""
    count = 1
    for i in range(1,len(current)):
        if current[i]==current[i-1]:
            count += 1
        else:
            string += str(count) + current[i-1]
            count = 1
    string += str(count) + current[-1]
    return string

for i in range(26):
    arr.append(get_next(current))
    current = arr[-1]

print(len(arr[30]))

#answer is 5808
