f=open('sample.txt','r',encoding='utf8')
sum = 0
scores = f.readlines()
f.close()

for i in scores:
    sum += int(i)

avg = sum/len(scores)
f = open('result.txt','w',encoding='utf8')
f.write(str(avg))
f.close()

