from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.museum import Museum
import repositories.museum_repository as museum_repository

museums_blueprint = Blueprint("museums", __name__)

# INDEX
# GET '/museums
@museums_blueprint.route('/museums')
def museums():
    museums = museum_repository.select_all()
    return render_template("museums/index.html", museums = museums)

# NEW
# GET '/museums/new'
@museums_blueprint.route("/museums/new", methods=['GET'])
def new_museum():
    return render_template("/museums/new.html")

# CREATE
# POST '/museums'
@museums_blueprint.route("/museums", methods=['POST'])
def create_museum():
    # get the information from the form
    name = request.form['name']
    address = request.form['address']
    # create a museum object with that information
    museum = Museum(name, address)
    # save the object to the data base
    museum_repository.save(museum)
    return redirect("/museums")

# SHOW
# GET '/museums/<id>'


# EDIT
# GET '/museums/<id>/edit'

# UPDATE
# PUT '/museums/<id>'

# DELETE
# DELETE '/museums/<id>'

