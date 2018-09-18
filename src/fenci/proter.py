#encoding=utf-8

from nltk.stem import PorterStemmer

count = 0

while(count < 500):        
    fr = open('C:\\Users\\Raytine\\Desktop\\En_out\\En_out'+str(count)+".txt", 'r')  
    fw =open('C:\\Users\\Raytine\\Desktop\\En_out2\\En_out2_'+str(count)+".txt", 'a') 

    for line in fr:    
        str1=line.strip()#读取文件的每一行
        print(str1)
        test = str1.split(" ")#将每个单词分离出来存入test数组
        for x in test:        #遍历test中的每一个单词
            porter = PorterStemmer()
            res = porter.stem(x) #抓取单词词干
            fw.write(res + " ")#写进文件
            print(res)  
    fr.close()
    fw.close()
    count = count + 1
print('done')