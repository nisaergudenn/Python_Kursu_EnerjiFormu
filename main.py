#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import (Flask, request, render_template)

app = Flask(__name__)


import pypyodbc

server = 'DESKTOP-I2FFSFS'
database = 'EnerjiForm'
port = '1433'  # SQL Server'ın kullandığı port numarası (genellikle 1433)

conn_str = "f Driver=SQL Server;Server={server},{port};Database={database};Trusted_Connection=yes;"

try:
    # SQL Server'e bağlanma
    conn = pypyodbc.connect(conn_str)

    # Bağlantıyı kullanarak bir imleç oluşturma
    cursor = conn.cursor()

    # SQL sorgusunu çalıştırma
    cursor.execute('SELECT * FROM gundem')

    # Sonuçları alıp yazdırma
    gundem_baslik = cursor.fetchall()
    for row in gundem_baslik:
        print(row)

    # Bağlantıyı kapatma
    conn.close()
    print("Bağlantı başarıyla sonlandırıldı.")

except pypyodbc.Error as e:
    print("Bağlantı hatası:", e)


@app.route('/')
def index():
    return render_template('anasayfa.html')

@app.route('/giris', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['sifre']

    if email in users and users[email] == password:
        return "<script>alert('Giris yaptınız');</script>"
    else:
        return "<script>alert('Hatalı mail veya sifre');</script>"



