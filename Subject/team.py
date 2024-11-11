from flask import Flask, request, render_template

app = Flask(__name__)

# 메인 페이지를 보여주는 경로
@app.route('/')
def index():
    return render_template('index.html')

# 학생 정보를 입력 페이지 경로
@app.route('/input')
def input():
    return render_template('input.html')

# 제출된 데이터를 처리하여 출력하는 경로
@app.route('/result', methods=['POST'])
def result():
    # 각 학생의 정보를 리스트로 받음
    names = request.form.getlist('name[]')
    student_numbers = request.form.getlist('StudentNumber[]')
    majors = request.form.getlist('major[]')
    emails = request.form.getlist('email[]')
    phone_number = request.form.getlist('phone_number[]')
    
    # 각 학생의 프로그래밍 언어와 역할을 가져오기 위해 리스트 생성
    genders = []
    programming_languages = []
    roles = []
    
    # 모든 학생 정보를 가져오기
    for i in range(len(names)):
        genders.append(request.form.getlist(f'gender[{i}]')[0]) # 성별 선택
        programming_languages.append(request.form.getlist(f'programming_language[{i}][]')) # 프로그래밍 언어 선택
        roles.append(request.form.getlist(f'role[{i}]')[0])  # 역할 선택

    # 모든 데이터를 조합하여 students 리스트 생성
    students = []
    for i in range(len(names)):
        students.append((
            names[i],
            student_numbers[i],
            majors[i],
            emails[i],
            phone_number[i],
            genders[i],
            ', '.join(programming_languages[i]),  # 배열을 문자열로 변환
            roles[i]
        ))

    # 결과 페이지로 전달
    return render_template('result.html', students=students)

# 연락 정보 페이지를 보여주는 경로
@app.route('/contact')
def contact_info():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)