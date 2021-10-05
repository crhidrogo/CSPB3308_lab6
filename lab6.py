from flask import Flask, request, jsonify, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
	return "<h1>Welcome to my app!</h1>"

@app.route("/form", methods=['POST', 'GET'])
def form():
	return render_template('form.html')

@app.route('/userdata/<username>')
def userdata(username):
	return render_template('user_data.html', form_data = form_data)

@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.method == 'GET':
		return f"<h1>Hello, Anonymous</h1><h2>Please go to <a href='/form'>form</a> first!</h2>\
		<p>This page should not be accessed directly. Please fill out the form with your information first. Thank you!</p>"

	elif request.method == 'POST':
		form_data = request.form
		print(request.form['name'])
		name = form_data.get('name', 'User')
		return redirect(url_for('login', username=name))

@app.route("/get_your_ip", methods=["GET"])
def get_your_ip():
	ip_add = request.remote_addr
	
	with open("ip_addresses.json", 'w') as file:
		file.write(str(jsonify({'ip':ip_add})))
	return f"<h1>Get your IP address</h1><p>Your IP address is {str(ip_add)}</p>"
