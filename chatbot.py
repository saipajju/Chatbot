import pyautogui
name = input("Hello! What's your name? ")
print(
    'Hi ' + name + " I am chatbot I am here to chat and have fun with you... Type skills to know chatbot skills  ")
while True:
    ask = (input('What can I do for you? ').lower())
    if ask == 'skills' :
        print('''
"play a game" or "1"to play a game
"sing a song" or "2"to hear a song
"calender " or "3" to see the calender
"tell a story" or "4" to hear a story
"search" or "5" to search in the web
"make a list" or "6"to remember things
"help me make a password" or "7" to make a password
    ''')
    game = ""
    if ask == 'play a game' :
        game = (input("""
    Which of these games?
    Minecraft Classic
    Roblox
    Kizi
    Classic Car Game
    """).lower())
    elif ask == '1' :
        game = (input("""
        Which of these games?
        Minecraft Classic
        Roblox
        Kizi
        Classic Car Game
        """).lower())
    if game == 'classic car game' :
        import game
    elif game == 'kizi' :
        import webbrowser
        webbrowser.open('https://kizi.com')
    elif game == 'roblox' :
        import webbrowser

        webbrowser.open('https://roblox.com')
    elif game == 'minecraft' :
        import webbrowser

        webbrowser.open('https://classic.minecraft.net/?join=PyrOKF480EO5ijkvplay ')
    if ask == 'sing a song' :
        import song
    elif ask == 'sing a song for me' :
        import song
    elif ask == 'sing a song for me chatbot' :
        import song
    elif ask == 'sing a song chatbot' :
        import song
    elif ask == '2' :
        import song
    if ask == 'show me this year calendar' :
        import my_calender
    elif ask == 'calendar' :
        import my_calender
    elif ask == 'this year calendar' :
        import my_calender
    elif ask == '3' :
        import my_calender
    if ask == 'tell a story' :
        import story
    elif ask == 'story' :
        import story
    elif ask == 'tell me a story chatbot' :
        import story
    elif ask == '4' :
        import story
    elif ask == "search" :
        import search
    elif ask == "5" :
        import search
    elif ask == "make a list" :
        import list
    elif ask == "6" :
        import list
    elif ask == "help me remember things" :
        import list
    elif ask == 'help me with calculations' :
        import calculator
    elif ask == "7" :
        import calculator
    elif ask == 'open applications' :
        import open
    elif ask == 'help me make a password' :
        import password_generator
    elif ask == '8' :
        import password_generator
    elif ask == 'settings':
        import password_settings
    elif ask == '9':
        import password_settings
    elif ask == 'bye':
        yes_or_no = input('Do you want to give feedback? ')
        if yes_or_no == 'yes':
            import feedback_system
            import end_process
            break
        else:
            import end_process
            break
    elif ask == 'end':
        yes_or_no = input('Do you want to give feedback? ')
        if yes_or_no == 'yes':
            import feedback_system
            import end_process
            break
        else:
            import end_process
            break
    elif ask == 'open google':
        print('Ok, opening google...')
        pyautogui.hotkey('ctrl' , 'shift' , 'g')
    elif ask == 'open task manager':
        print('Okay, Opening task manager')
        pyautogui.hotkey('ctrl' , 'shift' 'esc')
