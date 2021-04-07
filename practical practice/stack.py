array = []
original = [0,5,10,15,1,3,4,6,8,20]

def push(array):
    for i in original:
        if i % 5 == 0:
            array.append(i)

def pop(array):
    array.pop()

push(array)
pop(array)

print(array)
