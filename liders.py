from flask import Flask, render_template
app = Flask (__name__)

@app.route( '/listadecursos' )
def listadecursos ( ):
            return render_template("Lista de Cursos.html" )


@app.route('/detalhedecurso' )
def detalhedecurso ():
            return render_template( "Detalhe de Curso.html")

app.run( )
