from flask import Flask, render_template, request, redirect, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"


def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# ---------------- PUBLIC ROUTES ---------------- #

@app.route("/")
def home():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return render_template("public/about.html")


@app.route("/pricing")
def pricing():
    return render_template("public/pricing.html")


@app.route("/explore-kols")
def explore_kols():
    return render_template("public/explore-kols.html")


@app.route("/explore-campaigns")
def explore_campaigns():
    return render_template("public/explore-campaigns.html")


# ---------------- AUTH ---------------- #

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        db = get_db()

        user = db.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        ).fetchone()

        if user:

            session["user_id"] = user["id"]
            session["role"] = user["role"]

            if user["role"] == "kol":
                return redirect("/kol/dashboard")

            if user["role"] == "company":
                return redirect("/company/dashboard")

        else:
            flash("Incorrect email or password")
            return redirect("/login")

    return render_template("public/auth/login.html")

# ---------------- KOL REGISTER ---------------- #

@app.route("/register/kol", methods=["GET", "POST"])
def register_kol():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]
        name = request.form["name"]
        country = request.form["country"]
        niche = request.form["niche"]
        platform = request.form["platform"]

        db = get_db()

        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO users (email,password,role) VALUES (?,?,?)",
            (email, password, "kol")
        )

        user_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO kol_profiles (user_id,full_name,country,niche,platform) VALUES (?,?,?,?,?)",
            (user_id, name, country, niche, platform)
        )

        db.commit()

        flash("Registration successful")
        return redirect("/login")

    return render_template("public/auth/register-kols.html")

# ---------------- COMPANY REGISTER ---------------- #

@app.route("/register/company", methods=["GET", "POST"])
def register_company():

    if request.method == "POST":

        company = request.form["company"]
        email = request.form["email"]
        password = request.form["password"]
        website = request.form["website"]
        industry = request.form["industry"]
        country = request.form["country"]

        db = get_db()

        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO users (email,password,role) VALUES (?,?,?)",
            (email, password, "company")
        )

        user_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO company_profiles (user_id,company_name,website,industry,country) VALUES (?,?,?,?,?)",
            (user_id, company, website, industry, country)
        )

        db.commit()

        flash("Company registered successfully")
        return redirect("/login")

    return render_template("public/auth/register-company.html")
# ---------------- KOL DASHBOARD ---------------- #

@app.route("/kol/dashboard")
def kol_dashboard():

    if "role" not in session or session["role"] != "kol":
        return redirect("/login")

    return render_template("public/auth/kol/dashboard.html")


@app.route("/kol/profile")
def kol_profile():
    return render_template("public/auth/kol/profile.html")


@app.route("/kol/social")
def kol_social():
    return render_template("public/auth/kol/social.html")


@app.route("/kol/collaborations")
def kol_collaborations():
    return render_template("public/auth/kol/collaborations.html")


@app.route("/kol/messages")
def kol_messages():
    return render_template("public/auth/kol/messages.html")


@app.route("/kol/wallet")
def kol_wallet():
    return render_template("public/auth/kol/wallet.html")


@app.route("/kol/settings")
def kol_settings():
    return render_template("public/auth/kol/settings.html")

# ---------------- COMPANY DASHBOARD ---------------- #

@app.route("/company/dashboard")
def company_dashboard():

    if "role" not in session or session["role"] != "company":
        return redirect("/login")

    return render_template("public/auth/company/dashboard.html")


@app.route("/company/profile")
def company_profile():
    return render_template("public/auth/company/com_profile.html")


@app.route("/company/create_campaigns")
def company_create_campaigns():
    return render_template("public/auth/company/create_campaigns.html")


@app.route("/company/browse_kols")
def company_browse_kols():
    return render_template("public/auth/company/browse_kols.html")


@app.route("/company/campaigns")
def company_campaigns():
    return render_template("public/auth/company/campaigns.html")


@app.route("/company/wallets")
def company_wallets():
    return render_template("public/auth/company/wallets.html")


@app.route("/company/settings")
def company_settings():
    return render_template("public/auth/company/settings.html")


@app.route("/company/messages")
def company_messages():
    return render_template("public/auth/company/messages.html")

# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)