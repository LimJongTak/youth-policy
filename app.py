from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

# 아래에 추가되는 라우트와 뷰 함수들을 가져오기 위해 각 파일을 import
from login import *
from signup import *
from main import *
from customer_management import *
from customer_service import *
