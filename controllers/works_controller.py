from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.museum import Museum
from models.work import Work
import repositories.museum_repository as museum_repository
import repositories.work_repository as work_repository

works_blueprint = Blueprint("works", __name__)

# INDEX
# GET '/works
@works_blueprint.route('/works')
def works():
    works = work_repository.select_all()
    return render_template("/works/index.html", works = works) # added / before works

# NEW
# GET '/works/new'
@works_blueprint.route("/works/new", methods=['GET'])
def new_work():
    return render_template("/works/new.html", museums = museum_repository.select_all()) # added 
    
# CREATE
# POST '/works'
@works_blueprint.route("/works", methods=['POST'])
def create_work():
    # get the info from the form
    title = request.form['title']
    artist = request.form['artist']
    year = request.form['year']
    museum_id = request.form['museum_id'] # added museum_id instead of museum_repository

    # create the work objectwhich includes above info
    museums = museum_repository.select_all() # added
    work = Work(title, artist, year, museums[int(museum_id) - 1]) # museum_id changed to museums[int(museum_id) - 1])
    # save object to the db
    work_repository.save(work)
    return redirect("/works")


# SHOW
# GET '/works/<id>'

# EDIT
# GET '/works/<id>/edit'

# UPDATE
# PUT '/works/<id>'

# DELETE
# DELETE '/works/<id>'

