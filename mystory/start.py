from flask import Flask,render_template

app=Flask(__name__)


@app.route('/home')
def homepg():
    return render_template("home.html5")

@app.route('/login')
def loginpg():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
    