from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__, template_folder='C:/Users/Admin/Desktop/сайт/templates', static_folder='C:/Users/Admin/Desktop/сайт/static')

# PostgreSQL database configuration
db_config = {
    'dbname': 'Dropshipping',
    'user': 'postgres',
    'password': 'moyasemya56',
    'host': 'localhost'  # Change this to your PostgreSQL server host if not local
}

# Function to insert data into PostgreSQL
def insert_data(country, address, phone,  fullname, postcode):
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        
        # Example query to insert data
        query = "INSERT INTO payments (country, address, phone,  fullname, postcode) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (country, address, phone,  fullname, postcode))
        
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Error inserting data: {e}")
        return False

# Route to handle form submission
@app.route('/process_payment', methods=['POST'])
def process_payment():
    if request.method == 'POST':
        country = request.form['country']
        address = request.form['address']
        phone = request.form['phone']
        fullname = request.form['fullname']
        postcode = request.form['postcode']
        if insert_data(country, address, phone, fullname, postcode):
            # Determine where the form was submitted from
            referer = request.headers.get('Referer')


        
        if 'pay' in referer and 'pay2' in referer and 'pay1' not in referer:
            return redirect(url_for('Paybt3'))
        elif 'pay' in referer and 'pay1' in referer:
            return redirect(url_for('Paybt2'))
        elif 'pay' in referer and 'pay1' not in referer:
            return redirect(url_for('Paybt1'))
        else:
            return redirect(url_for('home'))
            
    else:
        return "Error processing payment"

'''
@app.route('/process_payment', methods=['POST'])
def process_payment():
    if request.method == 'POST':
        country = request.form['country']
        address = request.form['address']
        phone = request.form['phone']
        fullname = request.form['fullname']
        postcode = request.form['postcode']
        
        if insert_data(country, address, phone, fullname, postcode):
            # Determine where the form was submitted from
            referer = request.headers.get('Referer')

            if 'pay' in referer and 'pay2' in referer and 'pay3' in referer and 'pay1' not in referer:
                return redirect(url_for('Paybt4'))
            elif 'pay' in referer and 'pay2' in referer and 'pay1' not in referer:
                return redirect(url_for('Paybt3'))
            elif 'pay' in referer and 'pay1' in referer:
                return redirect(url_for('Paybt2'))
            elif 'pay' in referer and 'pay1' not in referer:
                return redirect(url_for('Paybt1'))
            else:
                return redirect(url_for('home'))
    else:
        return "Error processing payment"
'''


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/goods')
def Goods():
    return render_template('goods.html')

@app.route('/info')
def Info():
    return render_template('info.html')

@app.route('/about')
def About_us():
    return render_template('aboutus.html')

@app.route('/support')
def Support():
    return render_template('support.html')

@app.route('/first')
def First():
    return render_template('first.html')

@app.route('/second')
def Second():
    return render_template('second.html')

@app.route('/fourth')
def Fourth():
    return render_template('fourth.html')
'''
@app.route('/fifth')
def Fifth():
    return render_template('secornd.html')
@app.route('/sixth')
def Sixth():
    return render_template('secoend.html')
'''
@app.route('/third')
def Third():
    return render_template('third.html')

@app.route('/private_policy')
def Private_Policy():
    return render_template('privatepolicy.html')

@app.route('/terms')
def Terms_of_Use():
    return render_template('termsofservice.html')

@app.route('/pay')
def Pay1():
    return render_template('Pay.html')

@app.route('/paybt1')
def Paybt1():
    return render_template('paypalbutton.html')
@app.route('/paybt2')
def Paybt2():
    return render_template('paybtn2.html')
@app.route('/paybt3')
def Paybt3():
    return render_template('paybtn3.html')
'''
@app.route('/paybt4')
def Paybt4():
    return render_template('paybtn4.html')
'''
@app.route('/pay1')
def Pay2():
    return render_template('Pay2.html')
'''@app.route('/pay4')
def Pay4():
    return render_template('Pay4.html')'''
@app.route('/pay2')
def Pay3():
    return render_template('Pay3.html')
@app.route('/history')
def History():
    return render_template('history.html')

if __name__ == "__main__":
    app.run(debug=True)
