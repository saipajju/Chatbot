print('Welcome to the car game')
print('Type help for a list of commands')
car = ""
while True:
    car = input('> ').lower()
    if car == 'help':
        print('''start - to start the car
stop - to stop the car
quit - to exit  
            ''')
    elif car == 'start':
        print("Car has started...")
    elif car == 'stop':
        print('Car has stopped!')
    elif car == 'quit':
        print('The game has ended')
        break
    else:
        print("Sorry,I don't understand that!!")