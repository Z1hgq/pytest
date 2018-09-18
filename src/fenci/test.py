#encoding=utf-8
import jieba
   
   
count = 0

while(count < 10):    
    f =  open('C:\\Users\\Raytine\\Desktop\\En_out\\En_out'+str(count)+".txt", 'rb')  
    try:
        txt = f.read()
    finally:
        f.close()
    seg_list = jieba.cut(txt, cut_all=True)
    f2 =  open('C:\\Users\\Raytine\\Desktop\\En_out2\\En_out2'+str(count)+".txt", 'w') 
    try:
        f2.write(" ".join(seg_list))
    finally:
        f2.close()   
    print (" ".join(seg_list) ) # 全模式
    count = count + 1
print('done')

