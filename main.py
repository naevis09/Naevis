from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#koneksi ke database
app.secret_key = 'bebasapasaja'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'MUSIKU'
mysql = MySQL(app)

@app.route("/")
def home() -> str:
    return render_template('index.html')

#tampil data
@app.route("/admin")
def customertampildata() -> str:
    cur =mysql.connection.cursor()
    cur.execute("SELECT * FROM customer ORDER BY id DESC")
    data = cur.fetchall()
    cur.close
          
    return render_template('admin.html', datapemesan = data)



#insert into
@app.route('/', methods=['POST', "GET"])
def customermusikuinsert():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        phone = request.form['phone']
        type = request.form['type']
        date = request.form['date']
        jml = request.form['jml']
        ket = request.form['ket']
        foto = request.form['foto']

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png' , 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return'.' in filename and filename.rsplit('.' , 1)[1].lower() in ALLOWED_
    
     
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customer (nama, email, phone, type, date, jml, ket) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nama, email, phone, type, date, jml, ket))
        mysql.connection.commit()
        flash("Data Anda Berhasil Dikirim! Tunggu beberapa saat dan check email anda")
        return redirect(url_for('home'))
        

if __name__ == "__main__":
    app.run(debug=True)