#encoding=utf-8
from fenci import cos

#找出最大的5个数的位置，即离类中心最近的几个文档的位置
def getMax5Index(nums):
    temp=[]
    Inf = 0
    for i in range(5):
        temp.append(nums.index(max(nums)))
        nums[nums.index(max(nums))]=Inf
    print(temp)
    return temp

fileName = []#类中文件路径
dis = []#类中每一个文档与质心的距离
fr = open('C:\\Users\\Raytine\\Desktop\\max\\c12.txt','r')
for line in fr:    
        str1=line.strip()#��ȡ�ļ���ÿһ��
        test = str1.split(",")#��ÿ�����ʷ����������test����
        for x in test:        #����test�е�ÿһ������
            print(x)
            fileName.append(x)
c = cos.cosdis()
f = 'C:\\Users\\Raytine\\Desktop\\En_out2\\En_out2_11.txt'
for ele in fileName:
    d = c.cos(ele,f)
    dis.append(d)
print(dis)

for e in getMax5Index(dis):
    print(fileName[e]) 
