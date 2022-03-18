
class Database:
  database = None
  unique_id = 1
  
  def __init__(self):
    self.uuid = Database.unique_id
    Database.unique_id = Database.unique_id + 1
  
  @staticmethod
  def get_instance():
    if Database.database is None:
      Database.database = Database()
    return Database.database

  def query(self, statement):
    print('making query: ' + statement)
    print("db id: " + str(self.uuid))

class Application:
  @staticmethod
  def start():
    db = Database.get_instance()
    db.query('select * from users')

    other_db = Database.get_instance()
    other_db.query('select * from patters')

Application.start()