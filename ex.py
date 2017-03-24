# -*- coding: utf-8 -*-  

import requests

user_input = raw_input("请输入要查询的电影名称： ")

url = 'http://api.douban.com/v2/movie/search?q={%s}' % user_input
r = requests.get(url)
r_dict = r.json()

rating = r_dict['subjects'][0]['rating']['average']
id = r_dict['subjects'][0]['id']
images = r_dict['subjects'][0]['images']['large']

url2 = 'http://api.douban.com/v2/movie/subject/%s' % id
r2 = requests.get(url2)
r2_dict = r2.json()

ratings_count = r2_dict['ratings_count']

print """
电影评分：%r
评分人数：%d
电影海报：%r
""" % (rating, ratings_count, images)
