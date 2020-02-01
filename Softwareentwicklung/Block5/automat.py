regex1 = "c*b"
regex2 = "a(b|c)a"

def automat1(input):
    state = 0
    start_index = 0
    result = []
    for i,c in enumerate(input):
        if(state == 0 and c == "a"):
            state = 1
            start_index = i
        elif state == 1 and c == "c":
            state = 1
        elif state == 1 and c == "b":
            state = 0
            result.append((start_index, i))
        else: 
            state = 0 
    return result

def automat2(input):
    state = 0
    start_index = 0
    result = []
    for i,c in enumerate(input):
        if(state == 0 and c == "a"):
            state = 1
            start_index = i
        elif state == 1 and (c == "c" or c == "b"):
            state = 2
        elif state == 2 and c == "a":
            result.append((start_index, i))
        else: 
            state = 0 
    return result    

zeichenkette = "abals08zagaccccbo8azofhasdfacbab"
print(automat1(zeichenkette))
print(automat2(zeichenkette))