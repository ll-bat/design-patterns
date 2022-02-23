
class EventManager:
  listeners = dict()

  def subscribe(self, event_type, listener):
    if self.listeners.get(event_type, None) is None:
      self.listeners[event_type] = []
    self.listeners[event_type].append(listener)

  def unsubscribe(self, event_type, listener):
    self.listeners.get(event_type, []).remove(listener)

  def notify(self, event_type, data):
    for listener in self.listeners.get(event_type, []):
      listener.on_update(data)

class Database:
  event_manager = None

  def __init__(self):
    self.event_manager = EventManager()

  def on_connection(self):
    self.event_manager.notify('on_connection', self)

  def on_close(self):
    self.event_manager.notify('on_close', self)


class EventListener:
  def on_update(self, data):
    pass 

class LoggingEventListener(EventListener):
  def on_update(self, data):
    print('connection to database was established')

class App:
  def init(self):
    database = Database()
    logging_event_listener = LoggingEventListener()
    database.event_manager.subscribe('on_connection', logging_event_listener)
    database.on_connection()

app = App()
app.init()