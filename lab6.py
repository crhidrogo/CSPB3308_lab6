from flask import Flask, request, jsonify, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
	return "<h1>Welcome to my app!</h1>"

@app.route('/userdata/<username>')
def userdata(username,form_data):
	return render_template('user_data.html', form_data = form_data)

@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		form_data = dict(request.form)
		print(form_data)
		name = request.form['Name']
		print(name)
		#form_data = request.get_json()
		print(f"this is the result of result.get_json(): {form_data}")
		return redirect(url_for('userdata', username=name, form_data=form_data))
	else:
		username = request.args.get('name')
		return render_template('form.html')

@app.route("/get_your_ip", methods=["GET"])
def get_your_ip():
	ip_add = request.remote_addr
	
	with open("ip_addresses.json", 'w') as file:
		file.write(str(jsonify({'ip':ip_add})))
	return f"<h1>Get your IP address</h1><p>Your IP address is {str(ip_add)}</p>"
