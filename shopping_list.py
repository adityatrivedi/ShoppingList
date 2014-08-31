shopping_list = []

def show_help():
  print("What should we pick up at the store?")
  print("Enter DONE to stop. Enter HELP for this help. Enter SHOW to see your current list.")

def add_to_list(item):
  shopping_list.append(item)
  print("Added! List has {} items.".format(len(shopping_list)))


