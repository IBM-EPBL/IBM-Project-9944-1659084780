from flask import Flask,render_template, request, redirect, url_for, session
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=tqj08800;PWD=UKFB37LGZ3q0xHGy",'','')

app = Flask(__name__)

@app.route("/")
def log():
    return render_template('home.html')


@app.route('/loginn')
def loginn():
  return render_template('login.html')

@app.route('/reques')
def reques():
  return render_template('request.html')

@app.route('/donor')
def donor():
  return render_template('donor.html')

@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/register',methods = ['POST', 'GET'])
def register():
  if request.method == 'POST':

    name = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    age = request.form['age']
    bloodgroup = request.form['bloodgroup']
    address = request.form['place']
    password = request.form['password']
 
    sql = "SELECT * FROM register WHERE email =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('login.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO register VALUES (?,?,?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, email)
      ibm_db.bind_param(prep_stmt, 3, phone)
      ibm_db.bind_param(prep_stmt, 4, age)
      ibm_db.bind_param(prep_stmt, 5, bloodgroup)
      ibm_db.bind_param(prep_stmt, 6, address)
      ibm_db.bind_param(prep_stmt, 7, password)
      ibm_db.execute(prep_stmt)
    
    return render_template('login.html', msg="Data saved successfuly..Please login using your details")

@app.route('/plasmareq',methods = ['POST', 'GET'])
def plasmareq():
  if request.method == 'POST':

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    bloodgroup = request.form['bloodgroup']
    date = request.form['date']
    address = request.form['address']
    district = request.form['district']
    state = request.form['state']
    age = request.form['age']

    insert_sql = "INSERT INTO plasmarequest VALUES (?,?,?,?,?,?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, name)
    ibm_db.bind_param(prep_stmt, 2, email)
    ibm_db.bind_param(prep_stmt, 3, phone)
    ibm_db.bind_param(prep_stmt, 4, bloodgroup)
    ibm_db.bind_param(prep_stmt, 5, date)
    ibm_db.bind_param(prep_stmt, 6, address)
    ibm_db.bind_param(prep_stmt, 7, district)
    ibm_db.bind_param(prep_stmt, 8, state)
    ibm_db.bind_param(prep_stmt, 9, age)
    ibm_db.execute(prep_stmt)
    
    return render_template('home.html', msg="Data saved successfuly")


@app.route('/donorform',methods = ['POST', 'GET'])
def donorform():
  if request.method == 'POST':

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    bloodgroup = request.form['bloodgroup']
    date = request.form['date']
    address = request.form['address']
    district = request.form['district']
    state = request.form['state']
    age = request.form['age']

    insert_sql = "INSERT INTO donorform VALUES (?,?,?,?,?,?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, name)
    ibm_db.bind_param(prep_stmt, 2, email)
    ibm_db.bind_param(prep_stmt, 3, phone)
    ibm_db.bind_param(prep_stmt, 4, bloodgroup)
    ibm_db.bind_param(prep_stmt, 5, date)
    ibm_db.bind_param(prep_stmt, 6, address)
    ibm_db.bind_param(prep_stmt, 7, district)
    ibm_db.bind_param(prep_stmt, 8, state)
    ibm_db.bind_param(prep_stmt, 9, age)
    ibm_db.execute(prep_stmt)
    
    return render_template('home.html', msg="Data saved successfuly")

@app.route('/login',methods=['POST'])
def login():
  
    email = request.form['email']
    password = request.form['password']

    sql = "SELECT * FROM register WHERE email =? AND password=?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.bind_param(stmt,2,password)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    if account:
            return render_template('home.html') 
    else:
        return render_template('login.html', msg="Login unsuccessful. Incorrect username / password !") 