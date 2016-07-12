# _*_ coding:utf8 _*_
from whuDa import app
from flask import render_template
import sys

reload(sys)
sys.setdefaultencoding('utf8')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/hot')
def hot():
    return render_template("hot_questions.html")


@app.route('/wait-reply')
def wait_reply():
    return render_template("wait_reply.html")


@app.route('/topic')
def topic():
    return render_template("topic.html")


@app.route('/topic/<name>')
def topic_detail(name):
    return render_template('topic_detail.html')


@app.route('/topic-recent-week')
def recent_week_topic():
    return render_template("recent_week_topics.html")


@app.route('/topic-recent-month')
def recent_month_topic():
    return render_template("recent_month_topics.html")


@app.route('/help')
def help():
    return render_template("help.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/question/<id>')
def question_detail(id):
    return render_template("question_detail.html")


@app.route('/people/<name>')
def people(name):
    return 'person page.'


# 以下是开发用的临时路由，到时候会和上面合并用session判断返回不同的页面。

@app.route('/dynamic')
def dynamic():
    return render_template('/login/login-dynamic.html')


@app.route('/login-discover')
def login_discover():
    return render_template('/login/login-discover.html')


@app.route('/login-hot')
def login_hot():
    return render_template('/login/login-hot_questions.html')


@app.route('/login-wait-reply')
def login_wait_reply():
    return render_template('/login/login-wait_reply.html')


@app.route('/login-topic')
def login_topic():
    return render_template('/login/login-topic.html')


@app.route('/login-question-detail')
def aaa():
    return render_template('/login/login-question_detail.html')

