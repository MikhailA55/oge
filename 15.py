c=0
a=int(input())
for i in range(a):
  b=input() 
  if int(b)<=16 and not b.count("5"):
    c= c+int(b)
print(c) 
