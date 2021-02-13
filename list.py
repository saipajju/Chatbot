try:
    my_list = []
    number = int(input("How many items do you want in your list? "))
    for x in range(number) :
        items = input("item: ")
        my_list.append(items)
        print(my_list)

except Exception:
    print("You can only measure in number not in strings")