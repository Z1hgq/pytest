import jieba  


# jieba.load_userdict('userdict.txt')  
# 创建停用词list  
def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords  


# 对句子进行分词  
def seg_sentence(sentence):  
    sentence_seged = jieba.cut(sentence.strip())  
    stopwords = stopwordslist('C:\\Users\\Raytine\\Desktop\\hgd_sw.txt')  # 这里加载停用词的路径  
    outstr = ''  
    for word in sentence_seged:  
        if word not in stopwords:
            if word.__len__() != 1:  
                if word >= u'\u4e00' and word <= u'\u9fa5':#判断是否是汉字  
                    if word != '\t':  
                        outstr += word  
                        outstr += " "  
    return outstr  

inputs = open('C:\\Users\\Raytine\\Desktop\\Ch_test.txt', 'rb')  
outputs = open('C:\\Users\\Raytine\\Desktop\\hgd_out3.txt', 'w')  
try:
    for line in inputs:  
        line_seg = seg_sentence(line)  # 这里的返回值是字符串  
        outputs.write(line_seg + '\n')  
finally:
    outputs.close()  
    inputs.close()  