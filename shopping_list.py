#!/usr/bin/env python3

import sys

shoppingList = []

def show_help():
    print("What should we pick up at the store?")
    print("Enter DONE to stop. Enter HELP for this help. Enter SHOW to see your current list.")

def add_to_list(item):
    shoppingList.append(item)
    print("Added! List has {} items.".format(len(shoppingList)))

def show_list():
    print("Here's your list:")
    for item in shoppingList:
        print(item)

def save_to_file(textList):
    outfile = open("./shopping-list.txt", 'w')
    for item in textList:
        outfile.write("%s\n" % item)
    outfile.close


show_help()

while True:
    new_item = input("> ")
    if new_item == 'DONE':
        show_list();
        save_to_file(shoppingList);
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)
    continue
