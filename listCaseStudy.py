def display_menu():
    print("MENU")
    print("1.add to  first")
    print("2.add to end")
    print("3.insert in a pos")
    print("4.remove first")
    print("5.remove last")
    print("6.remove in a pos")
    print("7.remove an item")
    print("8.display the list")
    print("9.display the first k items")
    print("10.display the last k items")
    print("11.display items in a range")
    print("12.Exit")   

display_menu()
list_items = []

def add_first(item):
    list_items.insert(0,item)

def add_end(item):
    list_items.append(item)

def inset_to_pos(pos,item):
    list_items.insert(pos,item)

def remove_first():
    if not list_items:
        print("list is empty")
    else:    
        list_items.pop(0)

def remove_end():
    if not list_items:
        print("list is empty")
    else:    
        list_items.pop()

def remove_by_index(index):
    if index >= len(list_items):
                print("out of bond")
    else:
        list_items.pop(index)  

def remove_item(item):
    if item in  list_items:
        print(item,"is not in this list")
    else:    
        list_items.remove(item)

def display_list():
    for item in list_items:
            print(item)

def view_fK_items(k):
    print(list_items[:k])

def view_lK_items(k):
    print(list_items[-k:])

def view_items_inRange(low,up):
    print(list_items[low:up+1])

while True:    
    choice = int(input("Enter your choice : "))
    if choice == 1:
        item = input("Enter your first item : ")
        add_first(item)

    elif choice == 2:
        item = input("Enter your first item : ")
        add_end(item)

    elif choice == 3:
        pos = int(input("Enter the position : "))
        if pos >=len(list_items):
            print("out of bond")
        else:     
            item = input("Enter your first item : ")
            inset_to_pos(pos,item) 

    elif choice == 4:
        remove_first()

    elif choice == 5:
        remove_end()

    elif choice == 6:
        if not list_items:
            print("list is empty")
        else:
            index = int(input("Enter the index of the item to be removed"))
            remove_by_index(index)

    elif choice == 7:
        if not list_items:
            print("list is empty")
        else:
            item = input("enter item you want to remove")
            remove_item(item)

    elif choice == 12:
        break
    else:
        print("invalid choice")

print("Programm end")