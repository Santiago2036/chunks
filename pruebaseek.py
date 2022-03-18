
filee= open("prueba.txt",'r')

filee.seek(20)

print(filee.tell())
 
print(filee.readline())







filee.close()