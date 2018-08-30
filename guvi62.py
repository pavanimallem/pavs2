x=raw_input()
count=0
for i in x:
     if((i=='0') or (i=='1')):
     	count+=1
if(count==(len(x))):
	print("yes")
else:
	print("no")
