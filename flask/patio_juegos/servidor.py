from flask import Flask, render_template
app = Flask(__name__)                     
    
@app.route('/')                           
def index():
    return render_template('index.html')

@app.route('/play')                           
def play():
    return render_template('index.html')

@app.route('/play/<int:num>/<string:color>')                           
def repeat_square(num, color):
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)                   

