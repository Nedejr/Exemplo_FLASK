from flask import Flask


app = Flask(__name__)

from views import *

#colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)
