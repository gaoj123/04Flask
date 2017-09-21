from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/part1")
def goodMorning():
    return "Good Morning!"

@app.route("/part2")
def weekend():
    return "Have a great weekend!"

if __name__=="__main__":
    app.debug=True
    app.run()
