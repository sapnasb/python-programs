#text to binay converter

text= input("Enter text to convert to Binary: ") 

print(' sum'.join(format(ord(x), 'b') for x in text))