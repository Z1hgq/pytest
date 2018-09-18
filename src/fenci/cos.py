#encoding=utf-8
import numpy as np  
from scipy.spatial.distance import pdist  

class cosdis(object):
    def dropDuplicate(self,nums):
        dic = {}
        ptr = 0
        while True:
            if ptr>=len(nums):
                break
            if nums[ptr] in dic:
                nums.pop(ptr)
                ptr-=1
            else:
                dic[nums[ptr]]=1
            ptr+=1
    def cos(self,f1,f2):
        x = []
        y = []
        fr1 = open(f1, 'r')  
        for line in fr1:    
            str1=line.strip()#��ȡ�ļ���ÿһ��
            #print(str1)
            test = str1.split(" ")#��ÿ�����ʷ����������test����
            for i in test:        #����test�е�ÿһ������
                if i != '':
                    x.append(i)
        fr1.close()
        fr2 = open(f2, 'r')  
        for line in fr2:    
            str1=line.strip()#��ȡ�ļ���ÿһ��
            #print(str1)
            test = str1.split(" ")#��ÿ�����ʷ����������test����
            for i in test:        #����test�е�ÿһ������
                if i != '':
                    y.append(i)
        fr2.close()
        #print('x',x)  
        #print('y',y) 
        z = [] 
        for i in x:
            z.append(i)
        for i in y:
            z.append(i)
        self.dropDuplicate(z) 
        #print('z',z) 
        arr1 = []
        arr2 = []
        k = 0
        j = 0
        while(j < len(z)):
            arr1.append(k)
            arr2.append(k)
            j = j + 1
        #计算第一个文档的向量
        j = 0
        for e in z:
            for i in x:
                if i == e:
                    arr1[j] =  arr1[j]+1
            j = j+1
        #计算第二个文档的向量
        j = 0
        for e in z:
            for i in y:
                if i == e:
                    arr2[j] =  arr2[j]+1
            j = j+1
        #print(arr1)
        #print(arr2)
        # solution1  
        dist1 = np.dot(arr1,arr2)/(np.linalg.norm(arr1)*np.linalg.norm(arr2))  
        # solution2  
        dist2 = 1 - pdist(np.vstack([arr1,arr2]),'cosine')  
          
        #print('dist1',dist1)  
        #print('dist2',dist2)  
        return dist1