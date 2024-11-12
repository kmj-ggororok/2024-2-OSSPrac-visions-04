# 베이스 이미지 설정
FROM tiangolo/uwsgi-nginx-flask:latest

# 작업 디렉토리 설정
# WORKDIR /app

# 애플리케이션 파일 추가
COPY . /app

# 애플리케이션 실행 명령
# CMD ["python3", "./Subject/team.py"]