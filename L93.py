#the authors are Gwyn and Mac

def count_character(word,char):
    count=0
    index=0
    while index < len(word):
        if word [index]== char:
            count += 1
        index +=1
    return count
word = "bonobos"
char = "o"
print(count_character("bonobos", "o"))
