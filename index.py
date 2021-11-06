from flask import Flask, render_template
from niveis import nvl1, nvl2, nvl3

app = Flask(__name__)


@app.route('/nvlum')
def primeiro():
    
    return render_template('nivel-um.html',  produtora=nvl1, usuario="nvl-2")

@app.route('/nvldois')
def segundo():
    
    return render_template('nivel-dois.html',  produtora=nvl2)

@app.route('/nvltres')
def terceiro():
    
    return render_template('nivel-tres.html',  produtora=nvl3)

app.run(debug=True)