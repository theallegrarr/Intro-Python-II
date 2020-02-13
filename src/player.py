# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
  def __init__(self, name, room, inventory = None):
    self.name = name
    self.room = room
    self.inventory = inventory
  
  def getItem(self, name):
    self.inventory.append(Item(name))
  
  def listItems(self):
    if self.inventory == None:
      return 'no items collected by this player \n'
    else:
      for i in self.inventory:
        print(i)