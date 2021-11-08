from flask import Flask, render_template
from niveis import nvl1, nvl2, nvl3
from usuarios import usuario1, usuario2, usuario3

app = Flask(__name__)

logado = usuario1

@app.route('/nvlum')
def primeiro():
    
    return render_template('nivel-um.html',  produtora=nvl1, usuario=logado)

@app.route('/nvldois')
def segundo():
    
    return render_template('nivel-dois.html',  produtora=nvl2, usuario=logado)

@app.route('/nvltres')
def terceiro():
    
    return render_template('nivel-tres.html',  produtora=nvl3, usuario=logado)

app.run(debug=True)