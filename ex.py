# -*- coding: utf-8 -*-  

# # import Flask from the flask library
# from flask import Flask, render_template, request
#
# # Create a new Flask instance as a variable named app.
# # The name passed to the Flask app should be __name__.
# app = Flask(__name__)
#
# @app.route('/') # give the view a route of '/'
# def index(): # add a view function named index
#     return render_template('index.html') # make the view function return
#
#
# @app.route('/search/', methods=['GET', 'POST'])
#
# # def get_movie(user_input):
# #     r = requests.get('http://api.douban.com/v2/movie/search?q={user_input}')
#
# def search():
#     r = request.get('http://api.douban.com/v2/movie/search?q={rating}')
#     r_dict = r.json()
#     return render_template('search.html', rating=r_dict['subjects'][0]['rating']['average'])
#
# if __name__ == "__main__":
#     app.run(debug=True)


import requests

user_input = raw_input("请输入要查询的电影： ")

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

print rating, ratings_count, id, images
