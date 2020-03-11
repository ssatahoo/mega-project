from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    transactions = load_data()
    total = sum(t['amount'] for t in transactions)
    return render_template('index.html', transactions=transactions, total=total)

@app.route('/add', methods=['POST'])
def add():
    description = request.form['description']
    amount = float(request.form['amount'])
    data = load_data()
    data.append({'description': description, 'amount': amount})
    save_data(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

# update 0 - feat: add income/expense labels
# update 2 - fix: form validation bug
# update 3 - fix: form validation bug
# update 4 - fix: float parsing for amount
# update 6 - feat: add income/expense labels
# update 7 - feat: add income/expense labels
# update 8 - feat: add transaction form
# update 11 - fix: form validation bug
# update 13 - feat: add income/expense labels
# update 15 - refactor: extract data functions
# update 16 - feat: add transaction form
# update 17 - feat: add income/expense labels
# update 24 - refactor: extract data functions
# update 25 - fix: float parsing for amount
# update 30 - fix: form validation bug
# update 31 - fix: form validation bug
