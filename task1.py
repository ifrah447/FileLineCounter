
#task1
f=open('my_text.txt','wb')
a = ("this is my first text line\n")
f.writelines(a)
f.close()
#using readlines
f=open('my_text.txt','r')
lines=f.readlines()
count=0
for line in lines:
    count+=1
    print(count,line.strip())


f.close()
