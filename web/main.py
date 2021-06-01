from flask import Flask, render_template, request, session, redirect, url_for

import util

app = Flask(__name__)
app.secret_key = 'buackr1111'

@app.route("/")
def index():
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		if request.method == 'POST':
			return render_template('index.html')

#모집하기		
@app.route("/recruit", methods=['GET','POST'])
def recruit():
	if request.method == 'GET':
		with open('./test','r') as f:
			data = f.read()
			print(data)
		return render_template('모집하기.html', apikey=data)
	if request.method == 'POST':
		name_value = request.form['name']
		depart_value = request.form['departure']
		dest_value = request.form['destination']
		time_value = request.form['timeout']

		util.recruit_db(name_value, depart_value, dest_value, time_value)
		return redirect(url_for('mainpage'))
	else:
		temp1='db에 저장되어있는 블랙리스트 사용자 이름'
		temp2='db에 저장되어있는 블랙리스트 이유'
		temp3='db에 저장되어있는 블랙리스트 날짜'
		return render_template('index.html', black_name=temp1, black_reason=temp2,black_date=temp3)
		# retrun render_template('login.html')
		
#블랙리스트
@app.route("/", methods=['GET', 'POST'])
def declare():
	if request.method == 'GET':
		return render_template('블랙리스트.html')
	if request.method == 'POST':
		name_value = request.form['black_name']
		reason_value = request.form['black_reason']

	util.declare_db(name_value, reason_value )

#로그인
@app.route("/login",methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('로그인.html')
	else:
		id_value = request.form['userid']
		pw_value = request.form['userpw']
		try:
			ex_value = util.login_db(id_value)
			if ex_value:
				session['login_user'] = id_value
				return redirect(url_for('mainpage'))
	
		except Exception as e:
			return e

@app.route('/main')
def mainpage(): 
	if 'login_user' in session:
		if request.method == 'GET':
			return render_template('메인메뉴.html', user=session['login_user'])
	else:
		return redirect(url_for('login'))

#로그아웃
@app.route('/logout')
def logout(): 
	session.pop('login_user', None) 
	return redirect(url_for('form'))

@app.route('/form') 
def form(): 
	if 'login_user' in session: 
		return render_template('test.html')
	return redirect(url_for('login'))

@app.route("/register", methods=['GET','POST'])
def post():
	if request.method == 'GET':
		return render_template('회원가입.html')
	else:
		name_value = request.form['user_name']
		id_value = request.form['user_id']
		pw_value = request.form['user_pw']
		try:
			util.register_db(name_value, id_value, pw_value)
			return redirect(url_for('login'))
			
		except Exception:
			return ''' <script> alert("중복된 아이디가 존재합니다"); location.href="/register" </script> '''


if __name__ == "__main__":
	app.run(host="103.29.68.187", port="80", debug=True)
