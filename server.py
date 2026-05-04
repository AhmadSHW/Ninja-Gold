from flask import Flask, render_template, request, session, redirect
import random
from datetime import datetime


app = Flask(__name__)
app.secret_key = "keep_it_safe"

@app.route('/')
def index():
	if 'gold' not in session:
		session['gold'] = 0
		session['activities'] = []
	return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
	building = request.form['building']
	curr_gold = 0

	if building == 'farm':
		curr_gold = random.randint(10, 20)
	elif building == 'cave':
		curr_gold = random.randint(5, 10)
	elif building == 'house':
		curr_gold = random.randint(2, 5)
	elif building == 'casino':
		curr_gold = random.randint(-50, 50)

	session['gold'] += curr_gold

	#activity log
	timestamp = datetime.now().strftime("%Y/%m/%D%I:%M %p")
	if curr_gold >= 0:

		activity = {
			 'content': f"earned {curr_gold} golds from the {building}!({timestamp})", 
		'class':'green'
		}
	else:

		activity = { 'content': f"entered a casino and lost {abs(curr_gold)} golds ... ouch.({timestamp})", 
		'class':'red'
		}

		#sensi bonus:
	session['activities'].insert(0, activity)

	return redirect('/')

	# ninja bonus 
@app.route('/reset')
def reset():
	session.clear()
	return redirect ('/')


if __name__ == "__main__":
	app.run(debug=True)












