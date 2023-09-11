"""
Создать форму для регистрации пользователей на сайте. Форма должна содержать 
поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". 
При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
"""
from flask import Flask, render_template, request, make_response
from models import db, User
from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm, LoginForm
from markupsafe import escape


app = Flask(__name__)
app.config['SECRET_KEY'] = b'89761078a68c4412e8f210588f84132b2a6d6ea3d60afd9a51aa90aecc52167a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db.init_app(app)

csrf = CSRFProtect(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()   
    
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


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method =='POST': 
        username = request.form.get('username')
        password = request.form.get('password')
        if (username, password) in db():
            return "Вы вошли "
        return f'неправильный {escape(username)} логин или пароль'
    return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        existing_user = User.query.filter((User.name == name) | (User.email == email)).first()
        
        if existing_user:
            error_msg = 'Имя пользователя или адрес электронной почты уже существуют.'
            form.name.errors.append(error_msg)
            return render_template('register.html', form=form)

        user = User(name=name, email=email, password=password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return 'Вы успешно зарегистрировались'
    return render_template('register.html', form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')













