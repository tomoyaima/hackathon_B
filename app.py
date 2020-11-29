from flask import Flask, render_template #追加

app = Flask(__name__, static_folder='html/static', template_folder='html/templates')

@app.route('/login.html')
def login():
    #return name
    return render_template("login.html") #変更

@app.route('/signup.html')
def signup():
    #return name
    return render_template("signup.html") #変更

@app.route('/index.html')
def index():
    #return name
    return render_template("index.html") #変更

## おまじない
if __name__ == "__main__":
    app.run(debug=True)