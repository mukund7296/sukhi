var="abcdefghijklmnopqrstuvwxyz"
print(var[3:8])
print(var[3:])
print(var[:8])
print(var[:-22])
print(var[::4])

s="ryan thomas"
print(s.capitalize())
#beautifull syntax
output=s[0].upper()+s[1:5]+s[5:].capitalize()
print(output)
#beautifull syntax
output=s[0:-1]+s[-1].upper()
print(output)
#beautifull syntax
output=s[0:len(s)-1]+s[-1].upper()
print(output)
#beautifull syntax
output=s[0].upper()+s[1:len(s)-1]+s[-1].upper()
print(output)

#operator

s="ryan"+" thomas"+str(10)
print(s)

#string repetation operator
s="ryan thomas "

print(s*3)
#any order can be take  (str*int)
print(3*s)
#type error TypeError: can't multiply sequence by non-int of type 'str'
#print(s*s)
print("#"*50)
print("Ryan thomas software")
print("#"*50)