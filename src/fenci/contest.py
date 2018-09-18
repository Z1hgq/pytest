#encoding=utf-8
from fenci import cos
from dis import dis

def getMaxIndex(arr):
    i = 0
    maxIndex = 0
    max = arr[0]
    while(i < len(arr)):
        if arr[i] > max:
            max = arr[i]
            maxIndex = i
        i = i + 1
    return maxIndex

#500个文档路径
fileName = []
i = 0
while(i < 500):
    sttr = 'C:\\Users\\Raytine\\Desktop\\En_out2\\En_out2_'+str(i)+'.txt'
    fileName.append(sttr)
    i = i + 1
print(fileName)

#质心
centroid = []
i = 0
while(i < 20):
    centroid.append(fileName[i])
    i = i + 1
print(centroid)
#其他
others = []
i = 20
while(i < 500):
    others.append(fileName[i])
    i = i + 1
print(others)
#类
cls = [[] for i in range(20)]
i = 0
while(i < 20):
    cls[i].append(fileName[i])
    i = i + 1
print(cls)
c = cos.cosdis()
i = 0

dis = [[] for i in range(480)]
while(i < 480):
    j = 0
    while(j < 20):#计算每一个文档与质心文档的余弦距离
        d = c.cos(centroid[j], others[i])
        dis[i].append(d)
        j = j + 1
    print(dis[i])
    index = getMaxIndex(dis[i])#最大余弦距离的位置
    cls[index].append(others[i])#加入到与20个质心最近的那一个类中
    print(cls)
    #重新计算质心
    if len(cls[index]) > 2:#小于三不必重新计算
        cl = len(cls[index])
        k = 0
        sumDis1 = 0 #新加入的元素与其余元素的余弦距离
        sumDis2 = 0 #原来的质心与其余元素的余弦距离
        while(k < cl):
            sumDis1 = sumDis1 + c.cos(others[i], cls[index][k])
            sumDis2 = sumDis2 + c.cos(centroid[index],cls[index][k])
            k = k + 1
            print(k)
        if sumDis1 > sumDis2:
            centroid[index] = others[i]#如果新的元素与类里面所有元素余弦距离大于原来质心与所有元素余弦距离，则更换质心
    print(i)
    i = i + 1
print('OK')
print(cls)
k = 0
fres = open('C:\\Users\\Raytine\\Desktop\\res\\res.txt','a')
while(k < 20):
    i = len(cls[k])
    j = 0
    while(j < i):
        s = cls[k][j] + ','
        fres.write(s)
        j = j + 1
    fres.write('\n')
    k = k + 1
fres.close
fre = open('C:\\Users\\Raytine\\Desktop\\res\\re.txt','a')
for i in centroid:
    fre.write(i + ' ')
print('OK')
        
    
#c = cos.cosdis()
#f1 = 'C:\\Users\\Raytine\\Desktop\\En_out2\\En_out2_0.txt'
#f2 = 'C:\\Users\\Raytine\\Desktop\\En_out2\\En_out2_1.txt'
#dia = c.cos(f1, f2)
#print(dia)