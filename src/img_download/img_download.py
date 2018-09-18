#coding=utf-8  
  
import urllib.request  
 
from bs4 import BeautifulSoup  

def get_html(url): #网页内容抓取
    try:
        r = urllib.request.urlopen(url)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        # r.encoding = 'utf-8'
        return r.text
    except:
        print("Open Error!!!")
 
 
def get_content(url):
    """
    爬取每一类型小说排行榜，
    按顺序写入文件，
    文件内容为 小说名字+小说链接
    将内容保存到列表
    并且返回一个装满url链接的列表
    """
 
    url_list = []
    html = get_html(url)
    # 煮汤
    soup = BeautifulSoup(html,'lxml')
 
    # 看到历史类和完本类的小说与其他小说不在一个div，分开读取
    category_list = soup.find_all('div', attrs={'class:','index_toplist mright mbottom'})
    # 匹配历史和完本类别的数目
    histoty_finished_list = soup.find_all('div', attrs={'class:','index_toplist mbottom'})
 
    for cate in category_list:
        name = cate.find('div',attrs={'class:','toptab'}).span.string
        with open('novel_list.csv', 'a+') as f:
            f.write("\n小说种类：{} \n".format(name))
        # 通过id来对总排行榜进行定位,
        general_list = cate.find(style='display: block;')
        # 找到全部小说名字，发现她们全部都包含在li标签中
        book_list = general_list.find_all('li')
        # 循环遍历每一个小说的名字以及链接
        for book in book_list:
            link = 'http://www.qu.la/' + book.a['href']
            title = book.a['title']
            # 将所有文章的url地址保存在一个列表变量里
            url_list.append(link)
            # 这里使用a模式,防止清空文件
            with open('novel_list.csv','a') as f:
                f.write("小说名: {:<} \t 小说地址: {:<} \n".format(title, link))
    
    for cate in histoty_finished_list:
        name = cate.find('div', class_='toptab').span.string
        with open('novel_list.csv', 'a') as f:
            f.write("\n小说种类：{} \n".format(name))
        
        general_list = cate.find(style='display: block;') #找到总排行榜
        book_list = general_list.find_all('li')
        for book in book_list:
            link = 'http://www.qu.la/' + book.a['href']
            title = book.a['title']
            url_list.append(link)
            with open('novel_list.csv', 'a') as f:
                f.write("小说名：{:<} \t 小说地址：{:<} \n".format(title, link))
    return url_list 
 
def get_txt_url(url):
    """
    获取每个章节的url地址：
    并创建小说文件
    """
    url_list = []
    html = get_html(url)
    soup =BeautifulSoup(html,'lxml')
 
    lista = soup.find_all('dd')
    # dd是包含小说每一章节链接
    txt_name = soup.find('h1').text
    # h1 是小说标题
    with open ('小说/{}.txt'.format(txt_name),"a+") as f:
        print("小说:%s文件创建成功！" %txt_name)
        f.write('小说标题：{}\n'.format(txt_name))
    for url in lista:
        url_list.append('http://www.qu.la/' + url.a['href'])
 
    return url_list, txt_name
 
def get_one_txt(url, txt_name):
    """获取小说每个章节文本并写入到本地"""
 
    html = get_html(url).replace('<br/>', '\n')
    soup = BeautifulSoup(html,'lxml')
 
    try:
        txt = soup.find('div', id='content').text.replace('chaptererror();','')
        title = soup.find('title').text
        # 观察正文可知，里面的原文可以扣取出来
 
        with open ('小说/{}.txt'.format(txt_name),"a") as f:
            f.write(title+'\n\n')
            f.write(txt)
            print("当前小说:{} 当前章节:{} 已经下载完毕".format(txt_name,title))
    except:
        print("Something wrong")
 
def get_all_txt(url_list):
    """下载排行榜里所有的小说
        并保存为txt格式
    """
 
    for url in url_list:
        # 获取当前小说的所有章节目录
        # 并且声称小说头文件
        page_list, txt_name = get_txt_url(url)
        """
        for page_url in page_list:
        # 遍历每一篇小说，并下载到目录
            get_one_txt(page_url, txt_name)
            print('当前进度 {}% '.format(url_list.index(url) / len(url_list) * 100))
        """
 
def main():
    # 排行榜地址
    base_url = 'http://www.qu.la/paihangbang/'
    # 获取排行榜中所有小说链接
    url_list = get_content(base_url)
    #除去重复小说
    url_list = list(set(url_list))
    get_all_txt(url_list)
 
if __name__=='__main__':
    main()
