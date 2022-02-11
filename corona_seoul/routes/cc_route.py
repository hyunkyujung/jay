from flask import render_template, request, Blueprint
import corona_seoul.vaccine.cc_service as cc_service

service = cc_service.centerCheckService()

bp = Blueprint('corona_seoul', __name__, url_prefix='/corona_seoul') #라우트 등록 객체

@bp.route('/list', methods=['GET', 'POST'])
def list():
    centers = service.getCenterByList()
    return render_template('corona_seoul/list.html', centers=centers)

@bp.route('/detail/<int:id>', methods=['GET'])
def detail(id):
    print(id)
    c = service.getCenterById(id)
    print(c)
    return render_template('corona_seoul/detail.html', c=c)
