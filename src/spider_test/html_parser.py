#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
import urllib.parse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/[1-9][0-9]{4,}/main"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self, page_url, soup):
        res_data = {}
        #标题
        title_node = soup.find('span', class_= " ui-mr8 state")
        res_data['title'] = title_node.get_text()
        #详细内容
        detail_node = soup.find('div',class_="f-info")
        res_data['detail'] = detail_node.get_text()
        
        return res_data
