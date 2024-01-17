from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route("/")
def main(title="Home", content="Welcome to CMC web app"):
    return render_template("index.html", title=title, content=content)

@app.route("/forum")
def forum(title="Forum", content="Welcome to CMC forum"):
    return render_template("forum.html", title=title, content=content)

@app.route("/donations")
def donations(title="Donations", content="Welcome to CMC donations"):
    return render_template("donations.html", title=title, content=content)

@app.route("/meetings")
def meetings(title="Meetings", content="Welcome to CMC meetings"):
    return render_template("meetings.html", title=title, content=content)

@app.route("/motorcycleclubs")
def mcs(title="MCs", content="Welcome to CMC page where MCs can present themselves"):
    return render_template("mcs.html", title=title, content=content)

@app.route("/about")
def about(title="About", content="Here you can learn about CMC"):
    return render_template("about.html", title=title, content=content)

if __name__ == "__main__":
    app.run()