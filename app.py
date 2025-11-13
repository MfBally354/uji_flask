from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Halaman login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Cek username dan password
        if username == 'iqbal' and password == '12345':
            return redirect(url_for('success'))
        else:
            return render_template('login.html', error='Username atau password salah!')
    
    return render_template('login.html')

# Halaman setelah login berhasil
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

