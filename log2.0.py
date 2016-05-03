#coding:utf-8
import re

#Baiduspider 百度蜘蛛
#Googlebot  google蜘蛛
#360Spider  360蜘蛛
#Sogou    搜狗蜘蛛

def spider_log(day):
    #返回规定时间的所有蜘蛛的日志（包括百度和谷歌360搜狗）
    spider = []
    for line in open('text.log'):
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










print one_log(spider_log(3),'Baiduspider')