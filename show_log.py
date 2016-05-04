#!F:/jigoog/logforseo/logforseo
import log2
from flask import Flask, jsonify, render_template, request
import chartkick

app = Flask(__name__, static_folder=chartkick.js())
app.jinja_env.add_extension("chartkick.ext.charts")

@app.route('/')
@app.route('/index')
def index():
    data ={'11-7':300,'11-8':30,'11-9':700,'11-10':200,'11-11':500,'11-12':20,'11-13':370,'11-14':630,'11-15':30,'11-16':80}
    return render_template('show.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
