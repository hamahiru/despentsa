despensa = {'Ura':'0',
            'SinLactosa':'0',
            'Calcio':'0',
            'Desnata':'0',
            'PCocina':'0',
            'PKomuna':'0',
            'Film':'0',
            'Aluminio':'0',
            'Lentejak' :'0',
            'Garbanzos' :'0',
            'Macarrones':'0',
            'Piparrak':'0',
            'Esparragos':'0',
            'GelOro':'0',
            'GelNormal':'0',
            'GelGorria':'0',
            'Detergente':'0',
            'Suavizante':'0',
            'Txanpu':'0'
            }

def despensa_lista():
    return despensa

def update(prod,kop):
    despensa[prod] = kop
    return despensa

def update_lista(prod,kop):
    despensa[prod] = kop
    return despensa
