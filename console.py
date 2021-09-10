import pdb
from models.work import Work
from models.museum import Museum

import repositories.work_repository as work_repository
import repositories.museum_repository as museum_repository


#work_repository.delete_all()
#museum_repository.delete_all()

print(museum_repository.select_all())

pdb.set_trace()




