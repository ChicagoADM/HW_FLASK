"""
Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,подвал),
и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон.
"""
from flask import Flask, render_template
from flask import Flask, render_template, request, url_for, redirect, abort, flash, make_response, session
from pathlib import PurePath, Path

from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Main'}
    return render_template('index.html', **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Clothes'}
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Shoes'}
    return render_template('shoes.html', **context)


@app.route('/jacket/')
def jacket():
    context = {'title': 'Jacket'}
    return render_template('jacket.html', **context)

@app.route('/cookie_form/', methods=['GET', 'POST'])
def set_cookie():
    if request.method == 'POST':
        context = {'title': 'main', 'name': request.form.get('login')}
        name = request.form.get('login')
        response = make_response(render_template('index.html', **context))
        response.set_cookie(name, 'Python_dev')
        return response
    context = {'title': 'cookies'}
    return render_template('cookie_form.html', **context)


@app.route('/delcookie/')
def delcookie():
    context = {'title': 'cookies'}
    response = make_response(render_template('cookie_form.html', **context))
    response.set_cookie(*request.cookies, expires=0)
    return response


if __name__ == '__main__':
    app.run()














