from flask import render_template
from app import app

@app.route('/customer_management')
def customer_management():
    # 아래 코드에 고객 관리 페이지의 로직을 추가 가능.
    return render_template('customer_management.html')
