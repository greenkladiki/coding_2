from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)
filename = 'users_answers.csv'

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/answers', methods=['POST'])
def answers():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        komsa = request.form['komsa']
        sevas = request.form['sevas']
        krulo = request.form['krulo']
        shabla = request.form['shabla']
        savok = request.form['savok']
        fieldnames = ['имя','возраст','город','комса',
                      'севас','крыло','шабла','савок']
        with open(filename, 'a+', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'имя': name, 'возраст': age, 'город': city,
                             'комса': komsa, 'севас': sevas, 'крыло': krulo,
                             'шабла': shabla, 'савок': savok})
        return render_template('answers.html')

@app.route('/stats')
def stats():
    with open(filename, 'r', encoding='utf-8') as content:
        content = csv.reader(content)
        return render_template('stats.html', content=content)
    
@app.route('/json')
def json():
    dict_csv = {}
    fieldnames = ['name', 'age', 'city', 'komsa',
                  'sevas', 'krulo', 'shabla', 'savok']
    with open(filename, 'r+', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            dict_csv[name] = json.loads(json.dumps(row))
    return render_template('json.html', json=dict_csv)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/results', methods=['POST'])
def results():
    dict_csv = {}
    if request.method == 'POST':
        name = request.form['ask_name']
        city = request.form['ask_city']
        fieldnames = ['name', 'city']
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in reader:
                dict_csv[name] = json.loads(json.dumps(row))
        return render_template('results.html', results=dict_csv)

if __name__ == '__main__':
    app.run(debug=True)

# python /Users/new.aloha/Desktop/last_try/1.py
