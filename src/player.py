# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
  def __init__(self, name, room):
    self.name = name
    self.room = room
    self.inventory = []
  
  def getItem(self, item):
    self.inventory.append(item)

  def dropItem(self, item):
    self.inventory.remove(item)
  
  def listItems(self):
    if self.inventory == []:
      return 'no items collected by this player \n'
    else:
      for i in self.inventory:
        print(i)