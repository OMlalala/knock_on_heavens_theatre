# -*- coding: utf-8 -*-  

from flask import Flask
app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return 'Index Page'
#
# @app.route('/hello/')
# def hello():
#     return 'Hello World'
#
# @app.route('/user/<username>/')
# def show_user_profile(username):
#     return 'User %s' % username
#
# @app.route('/post/<int:post_id>/')
# def show_post(post_id):
#     return 'Post %d' % post_id
#


from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
    

if __name__ == "__main__":
    app.run(debug=True)