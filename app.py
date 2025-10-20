from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__, template_folder='/home/pjr/hayden/templates')

connect = sqlite3.connect('database.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS MENU (id INTEGER PRIMARY KEY, number INTEGER, percent REAL, rate REAL, spiciness REAL, remark TEXT)')

desired_entry_count = 3

with sqlite3.connect("database.db") as users:
    cursor = users.cursor()

    # Get the current number of entries
    cursor.execute(f'SELECT COUNT(*) FROM MENU')
    current_entry_count = cursor.fetchone()[0]

    # Insert new entries if the count is less than desired
    if current_entry_count < desired_entry_count:
        entries_to_add = desired_entry_count - current_entry_count
        for i in range(current_entry_count, desired_entry_count):
            cursor.execute("INSERT INTO MENU (number,percent,rate,spiciness,remark) VALUES (?,?,?,?,?)", (0,0,0,0,"."))
        users.commit()
        print("Initialization complete.")
    else:
        print("Table already has enough entries. No initialization needed.")

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/kfood')
def kfood():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM MENU')
    data = cursor.fetchall()
    print("kfood")
    print(data)
    return render_template("kfood.html", data=data)

@app.route('/kfood_m1', methods=['GET', 'POST'])
def kfood_m1():
    if request.method == 'POST':
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM MENU')
        data = cursor.fetchall()
        print("kfood_m1")
        print(data)
        number = data[0][1]+1
        total = data[0][1] + data[1][1] + data[2][1] + 1
        percent = int(number * 100 / total)
        percent2 = int(data[1][1] * 100 / total)
        percent3 = int(data[2][1] * 100 / total)
        if data[0][3] > 0:
            rate = int(8 * data[0][3] + 2 * int(request.form['rate'])) / 10
        else:
            rate = request.form['rate']
        if data[0][4] > 0:
            spiciness =  int(8 * data[0][4] + 2 * int(request.form['spiciness'])) / 10
        else:
            spiciness = request.form['spiciness']
        remark = request.form['remark']
        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("REPLACE INTO MENU \
            (id, number,percent,rate,spiciness,remark) VALUES (1,?,?,?,?,?)",
                           (number, percent, rate, spiciness, remark))
            cursor.execute("REPLACE INTO MENU \
            (id, number,percent,rate,spiciness,remark) VALUES (2,?,?,?,?,?)",
                           (data[1][1], percent2, data[1][3], data[1][4], data[1][5]))
            cursor.execute("REPLACE INTO MENU \
            (id, number,percent,rate,spiciness,remark) VALUES (3,?,?,?,?,?)",
                           (data[2][1], percent3, data[2][3], data[2][4], data[2][5]))
            users.commit()
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM MENU')
        data = cursor.fetchall()
        return render_template("kfood.html", data=data)
    else:
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM MENU')
        data = cursor.fetchall()
        total = data[0][1] + data[1][1] + data[2][1]
        return render_template("kfood_m1.html", data=data)

@app.route('/kfood_m2', methods=['GET', 'POST'])
def kfood_m2():
    if request.method == 'POST':
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM MENU')
        data = cursor.fetchall()
        print("kfood_m2")
        print(data)
        number = data[1][1]+1
        total = data[0][1] + data[1][1] + data[2][1] + 1
        percent = int(number * 100 / total)
        percent1 = int(data[0][1] * 100 / total)
        percent3 = int(data[2][1] * 100 / total)
        if data[1][3] > 0:
            rate = int(8 * data[1][3] + 2 * int(request.form['rate'])) / 10
        else:
            rate = request.form['rate']
        if data[1][4] > 0:
            spiciness =  int(8 * data[1][4] + 2 * int(request.form['spiciness'])) / 10
        else:
            spiciness = request.form['spiciness']
        remark = request.form['remark']
        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("REPLACE INTO MENU \
            (id, number,percent,rate,spiciness,remark) VALUES (2,?,?,?,?,?)",
                           (number, percent, rate, spiciness, remark))
            cursor.execute("REPLACE INTO MENU \
            (id, number,percent,rate,spiciness,remark) VALUES (1,?,?,?,?,?)",
                           (data[0][1], percent1, data[0][3], data[0][4], data[0][5]))
            cursor.execute("REPLACE INTO MENU \
            (id, number,percent,rate,spiciness,remark) VALUES (3,?,?,?,?,?)",
                           (data[2][1], percent3, data[2][3], data[2][4], data[2][5]))
            users.commit()
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM MENU')
        data = cursor.fetchall()
        return render_template("kfood.html", data=data)
    else:
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM MENU')
        data = cursor.fetchall()   
        return render_template("kfood_m2.html", data=data)

@app.route('/kfood_m3', methods=['GET', 'POST'])
def kfood_m3():
    if request.method == 'POST':
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM MENU')
        data = cursor.fetchall()
        print("kfood_m3")
        print(data)
        number = data[2][1]+1
        total = data[0][1] + data[1][1] + data[2][1] + 1
        percent = int(number * 100 / total)
        percent1 = int(data[0][1] * 100 / total)
        percent2 = int(data[1][1] * 100 / total)
        if data[2][3] > 0:
            rate = int(8 * data[2][3] + 2 * int(request.form['rate'])) / 10
        else:
            rate = request.form['rate']
        if data[2][4] > 0:
            spiciness =  int(8 * data[2][4] + 2 * int(request.form['spiciness'])) / 10
        else:
            spiciness = request.form['spiciness']
        remark = request.form['remark']
        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("REPLACE INTO MENU \
            (id, number,percent,rate,spiciness,remark) VALUES (3,?,?,?,?,?)",
                           (number, percent, rate, spiciness, remark))
            cursor.execute("REPLACE INTO MENU \
            (id, number,percent,rate,spiciness,remark) VALUES (1,?,?,?,?,?)",
                           (data[0][1], percent1, data[0][3], data[0][4], data[0][5]))
            cursor.execute("REPLACE INTO MENU \
            (id, number,percent,rate,spiciness,remark) VALUES (2,?,?,?,?,?)",
                           (data[1][1], percent2, data[1][3], data[1][4], data[1][5]))
            users.commit()
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM MENU')
        data = cursor.fetchall()
        return render_template("kfood.html", data=data)
    else:
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM MENU')
        data = cursor.fetchall()   
        return render_template("kfood_m3.html", data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    
    
