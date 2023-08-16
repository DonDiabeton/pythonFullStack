from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', row=8, col=8, color_1="color-1", color_2="color-2") 

@app.route('/<int:row>')
def row(row):
    return render_template('index.html', row=row, col=8, color_1="color-1", color_2="color-2")                    
       
@app.route('/<int:row>/<int:col>')
def row_col(row, col):
    return render_template('index.html', row=row, col=col, color_1="color-1", color_2="color-2")         

@app.route('/<int:row>/<int:col>/<string:color_1>/<string:color_2>')
def row_col_color(row, col, color_1, color_2):
    return render_template('index.html', row=row, col=col, color_1=color_1, color_2=color_2)         

if __name__ == '__main__':
    app.run(debug=True)
