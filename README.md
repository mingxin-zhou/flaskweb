Flaskweb
============
An easy to start yet [full-featured](#features) web framework

# Installation
```bash
pip install -U flaskweb

# or git clone and install; git pull for later updates
git clone git@github.com:Meteorix/flaskweb.git
pip install -e flaskweb
```

# Quickstart
基本语法与flask几乎一样，几行代码即可构建一个web服务器
```python
from flaskweb.app import create_app, gevent_run
from flask import render_template

app = create_app("debug")

@app.route("/")
def index():
    return render_template("main.html")

if __name__ == "__main__":
    gevent_run(app)
```
不一样的地方在于，上面的web服务器自带：
*   用户登录系统
*   orm/migrate
*   db管理页面
*   restapi/swaggerui
*   gevent服务器

|||
|-------|---------|
|![main](./docs/images/main.jpg)|![!login](./docs/images/login.jpg)|
|![!api](./docs/images/api.jpg) |![!admin](./docs/images/admin.jpg)|


try it:
```bash
cd simple
# 初始化数据库，会保存到simple/app.db
flask db init
flask db upgrade
flask db migrate
# 运行gevent服务器
python -u app.py
```
then visit http://127.0.0.1:5000/

A more [sophisticated example](./example)



# Features
*   flask
*   sqlalchemy
*   config
*   logger
*   user login
*   db admin
*   restful api with swagger ui
*   gunicorn/gevent deployment
*   use as a 3rd library
*   frontend with bootstrap/jquery

## todo
*   deployment: nginx/gunicorn
*   tensorflow/pytorch webapp sample
*   jwt
*   cythonize
*   pyinstaller
*   dockerfile

# Tutorial

to be continued...

# Thanks
*   https://github.com/miguelgrinberg/flasky
*   https://github.com/JackStouffer/Flask-Foundation
