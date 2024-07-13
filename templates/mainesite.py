from flask import Flask, render_template

app = Flask(__name__ ,template_folder='templates',)

@app.route('/info')
def index():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True)
