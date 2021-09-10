#from controllers.museums_controller import museums -- wrong import
from db.run_sql import run_sql

from models.museum import Museum
from models.work import Work
import repositories.museum_repository as museum_repository

# Write your functions here
# CREATE
def save(work):
    sql = "INSERT INTO works (title, artist, year, museum_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [work.title, work.artist, work.year, work.museum.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    work.id = id
    return work

# READ
def select_all():
    works = []
    sql = "SELECT * FROM works"
    results = run_sql(sql)

    museums_list = museum_repository.select_all()

    for row in results:
        work = Work(row['title'], row['artist'], row['year'], museums_list[row['museum_id'] - 1]) # check
        works.append(work)
    return works

# the function below asks for specific art work object
def select(id):
    work = None
    sql = "SELECT * FROM works WHERE id = %s"  # this line specifically ask for id
    values = [id]
    result = run_sql(sql, values)[0]

    museums = museum_repository.select_all()

    if result is not None:
        work = Work(result['title'], result['artist'], result['year'], museums[result['museum_id'] - 1]) # check
    return work


# UPDATE

# DELETE
def delete_all():
    sql = "DELETE  FROM works"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM works WHERE id = %s"
    values = [id]
    run_sql(sql, values)
