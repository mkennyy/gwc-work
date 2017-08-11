school_supplies = ["notebook", "pencils", "looseleaf"]
item_name = "notebook"

def onList(item_name, school_supplies):
  for item in school_supplies:
      if item == item_name:
           return True
      else:
           return False
print(onList(item_name, school_supplies))
