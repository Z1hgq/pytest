#encoding=utf-8
import jieba  


# jieba.load_userdict('userdict.txt')  
# 创建停用词list  
def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords  


# 对句子进行分词  
def seg_sentence(sentence):  
    sentence_seged = jieba.cut(sentence.strip())  
    stopwords = stopwordslist('C:\\Users\\Raytine\\Desktop\\google_sw.txt')  # 这里加载停用词的路径  
    outstr = ''  
    for word in sentence_seged:  
        if word not in stopwords:
            if word.__len__() != 1:                  
                if word != '\t':  
                    outstr += word  
                    outstr += " "  
    return outstr  

count = 0

while(count < 500):
    inputs = open('C:\\Users\\Raytine\\Desktop\\En\\En_'+str(count)+".txt", 'rb')  
    outputs = open('C:\\Users\\Raytine\\Desktop\\En_out\\En_out'+str(count)+".txt", 'w')  
    try:
        for line in inputs:  
            line_seg = seg_sentence(line)  # 这里的返回值是字符串  
            outputs.write(line_seg + '\n')  
    finally:
        outputs.close()  
        inputs.close()  
    count = count + 1
print('done')