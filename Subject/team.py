from flask import Flask, request, render_template

app = Flask(__name__)

# 최초 메인 페이지를 보여주는 루트 경로
@app.route('/')
def index():
    return render_template('index.html')  # 위 HTML 코드를 form.html 파일로 저장해야 합니다

# 학생 정보를 입력 페이지 경로
@app.route('/input')
def input():
    return render_template('input.html')

# 제출된 데이터를 처리하여 출력하는 경로
@app.route('/result', methods=['POST'])
def result():
    # 각 학생의 이름과 학번 데이터를 리스트로 받음
    name = request.form.getlist('name[]')
    student_number = request.form.getlist('StudentNumber[]')
    major = request.form.getlist('major[]')
    email = request.form.getlist('email[]')
    gender = request.form.getlist('gender[0]')
    programming_language = request.form.getlist('programming_language[0][]')
    role = request.form.getlist('role[0]')

    # 데이터를 템플릿으로 전달하여 출력 페이지 생성
    return render_template('result.html', students = zip(name, student_number, major, email, gender, programming_language, role))

# 팀 연락 정보 출력하는 경로 
@app.route('/contact')
def contact_info():
   return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)