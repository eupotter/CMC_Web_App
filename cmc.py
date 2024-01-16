from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/forum")
def forum():
    return render_template("forum.html")

@app.route("/donations")
def donations():
    return render_template("donations.html")

@app.route("/meetings")
def meetings():
    return render_template("meetings.html")

@app.route("/motorcycleclubs")
def mcs():
    return render_template("mcs.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()