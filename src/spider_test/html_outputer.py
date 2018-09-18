#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []


    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
            count = 0
            for data in self.datas:                  
                sttr = "C:\\Users\\Raytine\\Desktop\\qq_"+str(count)+".txt"
                fout = open(sttr, "w", encoding="utf-8")
                #fout.write("<td>%s</td>" %data['url'])  
                fout.write("%s"%data['title'] .encode('utf-8').decode("utf-8"))
                #fout.write("<td>%s</td>"%data['summary' ].encode('utf-8').decode('utf-8')) 
                fout.write("%s"%data['detail' ].encode('utf-8').decode('utf-8'))
                fout.write("/n")                    
                fout.close()
                count = count + 1

            