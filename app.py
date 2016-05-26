from flask import Flask
from despensa import despensa_lista
from despensa import update
from despensa import update_lista
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def despensa():
    lista = despensa_lista()
    return render_template('despensa.html', lista = lista)

@app.route('/update', methods=["POST"])
def update():
    if request.method == "POST":
        prod = request.json['prod']
        kop = request.json['kop']
        lista = update_lista(prod, kop)
        return render_template('despensa.html', lista = lista)
        # get url that the user has entered



if __name__ == '__main__':
    app.debug = False
    app.run()
