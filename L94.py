#the authors are Gwyn and Mac
index = 0
s = "Mind the gap!"
while index < len(s) and s[index] != "": #while index is less than the length of s and s of index is not equal to 0
    index +=1
print(s[:index])



def unit_dot(x):
   def find_period(y):
       index = 0
       while index < len(y):
           for ch in y:
               if ch== ".":
                   return index
               else:
                   index += 1

   location = find_period(x)
   return x [:location]

print(unit_dot("This is a long sentence. This is another. "))
print(unit_dot("this is a sentence"))




