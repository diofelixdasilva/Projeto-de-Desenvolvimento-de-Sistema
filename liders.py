from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
            return render_template("index.html")

@app.route('/disciplina')
def disciplina():
            return render_template("Disciplina.html") 
           
@app.route('/noticias')
def noticias():
            return render_template("Noticias.html")
app.run()