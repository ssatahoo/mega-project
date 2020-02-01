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
