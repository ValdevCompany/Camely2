from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Создание экземпляра Flask
app = Flask(__name__)

# Конфигурация для подключения к MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cev208:moyasemya56@localhost/cev208$default'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация SQLAlchemy
db = SQLAlchemy(app)

# Определение модели данных
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    postcode = db.Column(db.String(20), nullable=False)

# Создаем таблицы, если они не существуют
with app.app_context():
    db.create_all()

# Функция для вставки данных в базу данных
def insert_data(country, address, phone, fullname, postcode):
    try:
        new_payment = Payment(
            country=country,
            address=address,
            phone=phone,
            fullname=fullname,
            postcode=postcode
        )
        db.session.add(new_payment)
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error inserting data: {e}")
        return False

# Маршрут для обработки платежа
@app.route('/process_payment', methods=['POST'])
def process_payment():
    if request.method == 'POST':
        country = request.form['country']
        address = request.form['address']
        phone = request.form['phone']
        fullname = request.form['fullname']
        postcode = request.form['postcode']

        if insert_data(country, address, phone, fullname, postcode):
            # Определяем, откуда была отправлена форма
            referer = request.headers.get('Referer')
            if 'pay' in referer and 'pay2' in referer and 'pay1' not in referer:
                return redirect(url_for('paybt3'))
            elif 'pay' in referer and 'pay1' in referer:
                return redirect(url_for('paybt2'))
            elif 'pay' in referer and 'pay1' not in referer:
                return redirect(url_for('paybt1'))
            else:
                return redirect(url_for('home'))
    return "Error processing payment"

# Основные маршруты
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/goods')
def goods():
    return render_template('goods.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/about')
def about_us():
    return render_template('aboutus.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/first')
def first():
    return render_template('first.html')

@app.route('/second')
def second():
    return render_template('second.html')

@app.route('/third')
def third():
    return render_template('third.html')

@app.route('/pay')
def pay1():
    return render_template('Pay.html')

@app.route('/paybt1')
def paybt1():
    return render_template('paypalbutton.html')

@app.route('/paybt2')
def paybt2():
    return render_template('paybtn2.html')

@app.route('/paybt3')
def paybt3():
    return render_template('paybtn3.html')

@app.route('/history')
def history():
    return render_template('history.html')

if __name__ == "__main__":
    app.run(debug=True)

