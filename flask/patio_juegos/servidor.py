from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Página de Inicio' 

@app.route('/play/<int:num_boxes>/<color>')
def play(num_boxes, color):
    return render_template('index.html', num_boxes=num_boxes, box_color=color)

if __name__ == '__main__':
    app.run()