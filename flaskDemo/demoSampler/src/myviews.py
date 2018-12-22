#给Flask视图加装饰器
#1、定义1个装饰器
from flask import request, render_template
from wtforms import Form, simple, validators, widgets

# from src.myapp import app


def auth(func):
    print('我在上面')
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner


class LoginForm(Form):
    # 不同的字段 内部包含正则表达式 html5.EmailField | html5.DateTimeField...
    name = simple.StringField(
        label='用户名',
        validators=[  # 验证规则和错误提示信息
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),  # 前端页面显示的插件.TextArea
        render_kw={'class': 'form-control'}  # 设置form标签的class信息

    )

    # 不同的字段 内部包含正则表达式  html5.EmailField | html5.DateTimeField...
    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=8, message='用户名长度必须大于%(min)d'),
            # 自定义验证规则
            validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
                              message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')

        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

# @app.route('/',methods=['GET'])
@auth #注意如果要给视图函数加装饰器，一点要加在路由装饰器下面，才会被路由装饰器装饰
def first_flask():
    print('ffff')
    return 'Hello World'

# @app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()     #实例化 form验证类
        # return render_template('login.html', form=form)
        return render_template('page1/login1.html', form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate(): #判断是否验证成功？
            print('用户提交数据通过格式验证，提交的值为：', form.data)
        else:
            print(form.errors)
        # return render_template('login1.html', form=form)

