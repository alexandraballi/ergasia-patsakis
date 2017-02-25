a=raw_input("dwse arithmous xorismenous me komma")
b=a.split(",")
print b
for i in range(len(b)):
  if int(b[i])==0:
     b.append(b.pop(i))
print b
