#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
from flask import Flask, session, render_template, redirect, g, url_for
from flask import request


app = Flask(__name__)
app.secret_key = "minhemliganyckel"

from controller import Controller
controller = Controller()

# Make it easier to debug
app.debug = True
app.config.update(
    PROPAGATE_EXCEPTIONS=True
)


@app.before_request
def before_request():
    """Before request"""
    g.user = None
    if 'username' in session:
        g.user = session['username']


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    index route - with login form, otherwise redirects to 'home' """
    if g.user:
        return redirect(url_for('home'))
    if request.method == 'POST':
        if request.form['password'] == 'password':
            session['username'] = request.form['username']
            return redirect(url_for('home'))
    return render_template('index.html')

@app.route('/home')
def home():
    """ Home route """
    if g.user:
        return render_template('home.html')
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    """
    Logs out of the session and redirects to login form
    """
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route("/about")
def about():
    """ About route """
    if g.user:
        return render_template('about.html')
    return redirect(url_for('index'))

@app.route("/products", methods=["POST", "GET"])
def products():
    """ Products route """
    if g.user:
        if request.method == "POST":
            if request.form["name"] != "" \
            and request.form["p_type"] != "" \
            and request.form["specific"] != "":
                message = controller.add_product()
            else:
                message = "Vänligen fyll i alla fält."

        if request.method == "GET":
            p_id = request.args.get("del") # Här tar vi hand om parametern 'del'
            p_type = request.args.get("p_type")
            if p_id != None: #Om den är satt
                message = controller.remove_product(p_id, p_type) #så kallar vi på en funktion som tar bort raden
        try:
            message
        except NameError:
            message = ""
        return render_template("products.html", product_table=controller.fix_products_table(),\
        list_of_categories=controller.list_of_categories, message=message)
    return redirect(url_for('index'))

@app.route("/categories", methods=["POST", "GET"])
def categories():
    """ Categories route """
    if g.user:
        return render_template("categories.html",
                               category_table=controller.fix_category_table(),
                               list_of_categories=controller.list_of_categories)
    return redirect(url_for('index'))

@app.route("/staff", methods=["POST", "GET"])
def staff():
    """ Staff route """
    if g.user:
        if request.method == "POST":
            if request.form["name"] != "" and request.form["role"] != "":
                message = controller.add_staff()
            else:
                message = "Vänligen fyll i alla fält."
        if request.method == "GET":
            del_this_person = request.args.get("del")
            if del_this_person != None:
                message = controller.remove_staff(del_this_person)
        try:
            message
        except NameError:
            message = ""
        return render_template("staff.html",
                               staff_table=controller.fix_staff_table(),
                               message=message)
    return redirect(url_for('index'))

@app.route("/stock", methods=["POST", "GET"])
def stock():
    """ Stock route """
    if g.user:
        if request.method == "POST":
            if request.form["amount"] != "":
                message = controller.add_products_to_stock()
                return render_template("stock.html",
                                       stock_table=controller.fix_stock_table(),
                                       product_list=controller.get_list_of_products(), message=message)
        if request.method == "GET":
            del_from_stock = request.args.get("del")
            if del_from_stock != None:
                message = controller.remove_from_stock(del_from_stock)
        try:
            message
        except NameError:
            message = ""
        return render_template("stock.html",
                               stock_table=controller.fix_stock_table(), product_list=controller.get_list_of_products(),
                               message=message)
    return redirect(url_for('index'))

@app.route("/rent_products", methods=["POST", "GET"])
def rent_products():
    """Rent Products route"""
    if g.user:
        if request.method == "POST":
            if request.form["amount"] != "":
                message = controller.rent_product()
                return render_template("rent_products.html",
                                       staff_list=controller.get_list_of_staff(),
                                       stock_list=controller.get_list_of_stock(), message=message)
            else:
                message = "Vänligen fyll i mängd."
                return render_template("rent_products.html",
                                       staff_list=controller.get_list_of_staff(),
                                       stock_list=controller.get_list_of_stock(), message=message)

        return render_template("rent_products.html",
                               staff_list=controller.get_list_of_staff(), stock_list=controller.get_list_of_stock())
    return redirect(url_for('index'))

@app.route("/rented_products", methods=["POST", "GET"])
def rented_products():
    """Rented Products route"""
    if g.user:
        if request.method == "GET":
            return_this_product = request.args.get("return")
            if return_this_product != None:
                controller.return_product(return_this_product)
        return render_template("rented_products.html", rented_products_table=controller.fix_rented_products_table())
    return redirect(url_for('index'))

@app.route("/change_staff", methods=["POST", "GET"])
def change_staff():
    """Change Staff route"""
    if g.user:
        if request.method == "POST":
            message = controller.change_staff()
            return render_template("change_staff.html", staff_list=controller.get_list_of_staff(), message=message)
        return render_template("change_staff.html", staff_list=controller.get_list_of_staff())
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
