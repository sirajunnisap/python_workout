# def display_menu():
#     print("MENU")
#     print("1.add to  first")
#     print("2.add to end")
#     print("3.insert in a pos")
#     print("4.remove first")
#     print("5.remove last")
#     print("6.remove in a pos")
#     print("7.remove an item")
#     print("8.display the list")
#     print("9.display the first k items")
#     print("10.display the last k items")
#     print("11.display items in a range")
#     print("12.Exit")   

# display_menu()
# list_items = []

# def add_first(item):
#     list_items.insert(0,item)

# def add_end(item):
#     list_items.append(item)

# def inset_to_pos(pos,item):
#     list_items.insert(pos,item)

# def remove_first():
#     if not list_items:
#         print("list is empty")
#     else:    
#         list_items.pop(0)

# def remove_end():
#     if not list_items:
#         print("list is empty")
#     else:    
#         list_items.pop()

# def remove_by_index(index):
#     if index >= len(list_items):
#                 print("out of bond")
#     else:
#         list_items.pop(index)  

# def remove_item(item):
#     if item in  list_items:
#         list_items.remove(item)

#     else:    
#         print(item,"is not in this list")

# def display_list():
#     for item in list_items:
#             print(item)

# def view_fK_items(k):
#     print(list_items[:k])

# def view_lK_items(k):
#     print(list_items[-k:])

# def view_items_inRange(low,up):
#     print(list_items[low:up+1])

# while True:    
#     choice = int(input("Enter your choice : "))
#     if choice == 1:
#         item = input("Enter your first item : ")
#         add_first(item)

#     elif choice == 2:
#         item = input("Enter your first item : ")
#         add_end(item)

#     elif choice == 3:
#         pos = int(input("Enter the position : "))
#         if pos >=len(list_items):
#             print("out of bond")
#         else:     
#             item = input("Enter your first item : ")
#             inset_to_pos(pos,item) 

#     elif choice == 4:
#         remove_first()

#     elif choice == 5:
#         remove_end()

#     elif choice == 6:
#         if not list_items:
#             print("list is empty")
#         else:
#             index = int(input("Enter the index of the item to be removed"))
#             remove_by_index(index)

#     elif choice == 7:
#         if not list_items:
#             print("list is empty")
#         else:
#             item = input("enter item you want to remove")
#             remove_item(item)

#     elif choice == 12:
#         break
#     else:
#         print("invalid choice")

# print("Programm end")

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

list_items = []

while True :
    choice = int(input('Enter your choice : '))
    if choice == 1:
        item = input('enter your first item :')
        list_items.insert(0,item)
    
    elif choice == 2:
        item = input('Enter your last item : ')
        list_items.append(item)

    elif choice == 3:
        pos = int(input('Enter the position you want to add the item : '))
        if pos > len(list_items):
            print('out of the bond')
        else:
            item = input('enter the item you want to add : ')
            list_items.insert(pos,item)

    elif choice == 4:
        if not list_items:
            print("list is empty")
        else:
            list_items.pop(0)

    elif choice == 5:
        if not list_items:
            print("list is empty")
        else:
            list_items.pop()

    elif choice == 6:
        pos = int(input("Enter the postion you want to delete the item : "))
        if pos > len(list_items):
            print("out of the bond")
        else:
            list_items.pop(pos)
    
    elif choice == 7:
        if not list_items:
            print("list is empty")
        else:
            item = input("enter the item you want to delete : ")
            if item in list_items:
                  list_items.remove(item)
            else:
                print("item is not exist in the list")
    
    elif choice == 8:
        if not list_items:
            print("list is empty")
        else:
            print(list_items)
            for item in list_items:
                print(item)

    elif choice == 9 or choice == 10:
        if not list_items:
            print("list is empty")
        else:
            k = int(input("enter a number ")) 
            if k >= len(list_items):
                print("out of range")
            else:
                if choice == 9:
                    print(list_items[:k])
                else:
                     print(list_items[k:])

    elif choice == 11:
        if not list_items:
            print("list is empty")
        else:
            low = int(input("enter low range number ")) 
            up = int(input("enter up range number "))
            print(list_items[low:up+1])
    
    elif choice == 12:
        break
    
    else:
        print("invlaid syntax")

print("program end")