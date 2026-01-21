#read
file=open("textfile.txt","r")
content=file.readline()
content1=file.readlines()
print(content)
print(content1)
file.close()

#append
file=open("textfile.txt","a")
file.write("\n new line added.")
file.close()

#write
file=open("textfile.txt","w")
file.write("\n hello world")
file.close()


