from abc import ABC, abstractmethod

# -------------------------------------
class Button(ABC):

  @abstractmethod
  def click(self):
    pass

  @abstractmethod
  def render(self):
    pass 


class HtmlButton(Button):
  def click(self):
    print("HtmlButton clicked")

  def render(self):
    print("HtmlButton render")


class MailButton(Button):
  def click(self):
    print("MailButton clicked")
  
  def render(self):
    print("MailButton render")
# -------------------------------------

# creation logic 
class Factory(ABC):
  def render(self):
    button = self.get_button()
    button.click()
    button.render()

  
  @abstractmethod
  def get_button(self) -> Button:
    pass 

class HtmlButtonFactory(Factory):
  def get_button(self):
    return HtmlButton()


class MailButtonFactory(Factory):
  def get_button(self):
    return MailButton()
# ---------------------------------------


class Application:
  def __init__(self):
    self.target = None

  def beforeStart(self):
    something = True
    other = False

    if something is True:
      self.target = HtmlButtonFactory()

    if other is True:
      self.target = MailButtonFactory()

  def execute(self):
    self.target.render()

  def start(self):
    self.beforeStart()
    self.execute()

    

application = Application()
application.start()