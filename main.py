from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
      return render_template('home.html')




if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='5000')
