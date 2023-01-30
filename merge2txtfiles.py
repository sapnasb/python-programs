# Python program to merge two files 
data = data2 = "" 
  
# Reading data from first file 
with open('b.txt') as fp: 
    data = fp.read() 
    
with open('a.txt') as fp: 
    data2 = fp.read() 
# Merging two files into one another file 
    data += "\n"
    data += data2 
    
with open ('ab.txt', 'w') as fp: 
    fp.write(data)