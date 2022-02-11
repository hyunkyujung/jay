#main역할 하는 파일

from flask import Flask, render_template
import routes.cc_route as cr
import routes.status_route as sr


app = Flask(__name__) # flask 객체 생성. 웹 서버를 포함한 app

app.register_blueprint(cr.bp) # 블루프린트를 Flask 객체에 등록
app.register_blueprint(sr.bp)
@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()#flask 서버 실행