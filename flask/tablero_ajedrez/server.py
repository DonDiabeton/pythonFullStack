from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/<int:x>/<int:y>')
def chessboard(x, y):

  return render_template('index.html', rows=x, cols=y)
  
if __name__ == '__main__':
  app.run(debug=True)