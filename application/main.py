import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template("index.html"))    

    
    
if __name__ == "__main__":
    hostname= os.environ.get('HOSTNAME', 'localhost')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=hostname, port=port)
