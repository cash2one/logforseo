#coding:utf-8
import re

#Baiduspider 百度蜘蛛
#Googlebot  google蜘蛛
#360Spider  360蜘蛛
#Sogou    搜狗蜘蛛

def spider_log(day):
    #返回规定时间的所有蜘蛛的日志（包括百度和谷歌360搜狗）
    spider = []
    for line in open('access.log'):  #修改日志文件位置
        line = line.strip()
        if re.findall(r'{day}/May/2016'.format(day=day),line):
            if re.findall(r'Baiduspider',line) or re.findall(r'Googlebot',line) or re.findall(r'360Spider',line) or re.findall(r'Sogou',line):
                spider.append(line)

    return spider


def one_log(spiders,search):
    #获得规定搜索引擎的所有蜘蛛
    one_spider = []
    for spider in spiders:
        if re.findall(search,spider):
             one_spider.append(spider)
    return one_spider



def bad_log(spiders):
    #获得404蜘蛛日志
    bad_spider = []
    for spider in spiders:
        if re.findall(r'404',spider):
            bad_spider.append(spider)
    return bad_spider

def bad_log(spiders):
    #获得正常的蜘蛛日志
    nice_spider = []
    for spider in spiders:
        if re.findall(r'200',spider) and not re.findall(r'.css',spider) and not re.findall(r'.jss',spider):
            nice_spider.append(spider)
    return nice_spider

def other_log(spiders):
    #获得其他蜘蛛日志
    other_spider = []
    for spider in spiders:
        if not re.findall(r'200',spider) and not re.findall(r'400',spider):
            other_spider.append(spider)
    return other_spider



def download_log(spiders):
    #通过正则表达式把日志分解成需要的模块
    re_download = '\s(\d+)\s"'
    download = 0
    for spider in spiders:
        if  re.findall(re_download,spider):
             download = int(re.findall(re_download,spider)[0]) + download
    return download


def url_log(spiders):
    #返回一个所有url的词典，没有经过排序
    url = {}
    for spider in spiders:
        if re.findall(r'\s/(.*?)\sHTTP/1.1',spider):
            lianjie = re.findall(r'\s/(.*?)\sHTTP/1.1',spider)[0]
            if lianjie not in url:
                url[lianjie] = 1
            else:
                url[lianjie] = url[lianjie] + 1
    return url

print download_log(spider_log(3))

#Baiduspider 百度蜘蛛
#Googlebot  google蜘蛛
#360Spider  360蜘蛛
#Sogou    搜狗蜘蛛
# print spider_log(3)[1]
