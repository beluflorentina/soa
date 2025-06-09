from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# 🔗 Conectare la baza de date
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="001F123Belu",
    database="BDTelecomunicatii"
)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/clienti")
def afiseaza_clienti():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Clienti")
    clienti = cursor.fetchall()
   # return render_template("db_clienti.html", clienti=clienti)
    return render_template("tabel.html", titlu="Clienti", coloane=clienti[0].keys() if clienti else [], date=clienti)


@app.route("/abonamente")
def abonamente():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Abonamente")
    data = cursor.fetchall()
    return render_template("tabel.html", titlu="Abonamente", coloane=data[0].keys() if data else [], date=data)

@app.route("/cartele")
def cartele():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM CartelePreplatite")
    data = cursor.fetchall()
    return render_template("tabel.html", titlu="Cartele Preplătite", coloane=data[0].keys() if data else [], date=data)

@app.route("/servicii")
def servicii():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Servicii")
    data = cursor.fetchall()
    return render_template("tabel.html", titlu="Servicii", coloane=data[0].keys() if data else [], date=data)

@app.route("/tarife")
def tarife():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Tarife")
    data = cursor.fetchall()
    return render_template("tabel.html", titlu="Tarife", coloane=data[0].keys() if data else [], date=data)

@app.route("/contracte")
def contracte():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Contracte")
    data = cursor.fetchall()
    return render_template("tabel.html", titlu="Contracte", coloane=data[0].keys() if data else [], date=data)

@app.route("/facturi")
def facturi():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Facturi")
    data = cursor.fetchall()
    return render_template("tabel.html", titlu="Facturi", coloane=data[0].keys() if data else [], date=data)

@app.route("/numere")
def numere():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM NumereTelefon")
    data = cursor.fetchall()
    return render_template("tabel.html", titlu="Numere de Telefon", coloane=data[0].keys() if data else [], date=data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

