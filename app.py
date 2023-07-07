from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('absensi.db')
        print("Koneksi ke database berhasil.")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table():
    conn = create_connection()
    query = '''
    CREATE TABLE IF NOT EXISTS absensi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        tanggal INTEGER NOT NULL,
        bulan INTEGER NOT NULL,
        tahun INTEGER NOT NULL
    );
    '''
    try:
        conn.execute(query)
        print("Tabel berhasil dibuat.")
    except sqlite3.Error as e:
        print(e)

create_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nama = request.form['nama']
        tanggal = int(request.form['tanggal'])
        bulan = int(request.form['bulan'])
        tahun = int(request.form['tahun'])

        save_absensi(nama, tanggal, bulan, tahun)

        return render_template('terimakasih.html')

    return render_template('index.html')

def save_absensi(nama, tanggal, bulan, tahun):
    conn = create_connection()
    query = "INSERT INTO absensi (nama, tanggal, bulan, tahun) VALUES (?, ?, ?, ?)"
    try:
        conn.execute(query, (nama, tanggal, bulan, tahun))
        conn.commit()
        print("Data absensi berhasil disimpan.")
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    app.run(debug=True)
