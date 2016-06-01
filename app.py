from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from database_setup import Base, StockDespensa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'DATABASE_URL'
db = SQLAlchemy(app)


engine = create_engine('DATABASE_URL')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def despensa():
    items = session.query(StockDespensa)
    lista = dict([ (i.name, i.kopurua) for i in items ])
    return render_template('despensa.html', lista = lista)

@app.route('/update', methods=["POST"])
def update():
    if request.method == "POST":
        prod = request.json['prod']
        kop = request.json['kop']
        items = session.query(StockDespensa)
        if  session.query(StockDespensa).filter(StockDespensa.name == prod).count():
            reg = session.query(StockDespensa).filter_by(name=prod).first()
            reg.kopurua = kop
            session.commit()
        items = session.query(StockDespensa)
        lista = dict([ (i.name, i.kopurua) for i in items ])
        return render_template('despensa.html', lista = lista)
        # get url that the user has entered



if __name__ == '__main__':
    app.debug = False
    app.run()
