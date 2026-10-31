#Sort a dictionary by its values in ascending order

d={"a":100,"b":30,"c":20,"d":40,"e":10}
item=list(d.items())

for i in range (len(item)):
    for j in range(i+1,len(item)):
        if item[i][1] > item[j][1]:
            item[i],item[j]=item[j],item[i]

result={}
for k,v in item:
    result[k]=v
print(result)
