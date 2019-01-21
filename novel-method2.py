# -*- coding:UTF-8 -*-
# soup.find_all 搜索到返回的为bs4.element.ResultSet类型对象
# soup.select 搜索到返回的为list类型对象
# 二者数据内容完全一样，type不一样

import requests
from bs4 import BeautifulSoup, ResultSet

base_url = 'https://www.lingyutxt.com/book_1/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


def get_novel_chapters(url):
    novellist = requests.get(url, headers=headers)
    novellist.encoding = 'gbk'
    '''拿到HTML数据'''
    soup_nl = BeautifulSoup(novellist.content, 'lxml')
    lists = soup_nl.select('#list dd')
    del lists[0:9]
    chapters = []
    for list in lists:
        chapters.append(list.a['href'])
    '''将小说章节对应后缀网址存入list并且返回该list'''
    return chapters

def get_chapter_text(url):
    chapter = requests.get(url, headers=headers)
    chapter.encoding = 'gbk'
    soup_chap = BeautifulSoup(chapter.content, 'lxml')

    bookname = soup_chap.select('.bookname h1')[0].text.replace('正文','')
    content = soup_chap.select('#content')[0].text
    content = bookname + '\n' + content

    return content





if __name__ == '__main__':

    base_url = 'https://www.lingyutxt.com/book_1/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    chapters = get_novel_chapters(base_url)
    n = 1
    for chapter in chapters:
        chapter_url = base_url + chapter
        chapter_content = get_chapter_text(chapter_url)
        with open('./灵域1.txt', 'a+',encoding='utf-8') as f:
           f.write(chapter_content+'\n\n')
        print('第{}章已写入。'.format(n))
        n += 1