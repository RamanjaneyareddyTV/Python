# file Handling
'''modes:
r
a
w
b
'''
#read
'''f=open("venkat.txt",'r')
print(f.readlines(20))
f.close()
'''
#write
'''
f=open("venkat.txt",'w')
f.write("this is venkat")
f.close()
f=open("venkat.txt",'r')
print(f.read())
'''
#append
'''f=open("venkat.txt",'a')
f.write("this is kiran")
f.close()
f=open("venkat.txt",'r')
print(f.read())'''
'''with open("venkat.txt") as f:
    print(f.read())'''
    
"machine learning"
'''save in txt file'''
"guess game"
