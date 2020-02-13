# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
from shutil import get_terminal_size

cols, rows = get_terminal_size()

class NewRoom:
  def __init__(self, name, description,
                 n_to=None, s_to=None,
                 e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.visible_items = []
  def __directions__(self):
      divider = "_" * (cols - 1)
      return    divider + "\n" \
              + f"{self.n_to.name if self.n_to else ' '}".center(cols) + "\n" \
              + f"{self.w_to.name if self.w_to else ' '}".ljust(cols) \
              + f"<-- You -->".center(cols) \
              + f"{self.e_to.name if self.e_to else ' '}".rjust(cols) + "\n" \
              + f"{self.s_to.name if self.s_to else ' '}".center(cols) + "\n" \
              + divider

  def __str__(self):
    return f'{self.name} {self.n_to} {self.s_to}'
  
  def __addItem__(self, item):
    self.visible_items.append(item)
  
  def __dropItem__(self, item):
    for x in self.visible_items:
      if x.name == item.name:
        self.visible_items.remove(x)

  def __getItems__(self):
    if self.visible_items is None or len(self.visible_items) == 0:
      return "No items in current room"
    else:
      return f"Items in current room: {[x.name for x in self.visible_items]}"