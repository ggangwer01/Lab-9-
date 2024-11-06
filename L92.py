#the authors are Gwyn and Mac

def word_triangle(word):
    length = len(word)
    while length > 0:
        print(word[:length])
        length -=1

print(word_triangle("Balloon"))


