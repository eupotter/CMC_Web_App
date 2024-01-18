from flask import Flask, render_template, request, redirect, url_for, request, session, flash
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "AskfJj90-@" #secret key for the session
app.permanent_session_lifetime = timedelta(days=5) #sets for how long the permanent session keeps the log in data

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

@app.route("/login", methods =["POST", "GET"])
def login(title="Log In"):
    if request.method == "POST":
        session.permanent = True #enable the permanent session
        user = request.form["nm"] #get the user from the login form
        session["user"] = user #assign the user to the session
        flash("You have been succesfully logged in.")
        return redirect(url_for("user")) #redirect to user page
    else:
        if "user" in session: #check if a user loged in or not in case the user wants to access /user page
            flash("Already logged in.")
            return redirect(url_for("user")) #if yes we redirect to user page
        return render_template("login.html", title=title) #else we render the log in page

@app.route("/user")
def user(title = "Settings"):
    if "user" in session: #checks if any user is loged
        user = session["user"] #assigns the user from session to user var
        return render_template("user.html", title=title, user=user) #displays the var
    else:
        flash("You are not logged in.")
        return redirect(url_for("login")) #if no user is loged in redirects to log in page

@app.route("/logout")
def logout():
    if "user" in session: #checks if user is loged in to make sure we do not show the log out message if noone was logged out
        user = session["user"]
        flash(f"You have been succesfully logged out. See you soon {user}!", "info")
    session.pop("user", None) #remove the user from the session
    return redirect(url_for("login")) #redirect to log in page

if __name__ == "__main__":
    app.run()