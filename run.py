from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='الرئيسية')

@app.route('/kali-install')
def kali_install():
    return render_template('kali_install.html', title='تثبيت كالي')

@app.route('/protection/accounts')
def protection_accounts():
    return render_template('protection_accounts.html', title='حماية الحسابات')

@app.route('/cyber-attacks')
def cyber_attacks():
    return render_template('cyber_attacks.html', title='الهجمات السيبرانية')

@app.route('/tools')
def tools():
    return render_template('tools.html', title='أدوات الحماية')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
