from db.run_sql import run_sql

from models.museum import Museum
from models.work import Work
import repositories.work_repository as work_repository


# Write your functions here

# CREATE
def save(museum):
    sql = "INSERT INTO museums (name, address) VALUES (%s, %s) RETURNING *"
    values = [museum.name, museum.address]
    results = run_sql(sql, values)
    id = results[0]['id']
    museum.id = id
    return museum

# READ
def select_all():
    museums = []
    sql = "SELECT * FROM museums"
    results = run_sql(sql)

    for row in results:
        museum = Museum(row['name'], row['address'], row['id'])
        museums.append(museum)
    return museums

# the function below asks for specific art work object
def select(id):
    museum = None
    sql = "SELECT * FROM museums WHERE id = %s"  # this line specifically ask for id
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        museum = Museum(result['name'], result['address'], result['id'])
    return museum

# UPDATE

# DELETE
def delete_all():
    sql = "DELETE  FROM museums"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM museums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


