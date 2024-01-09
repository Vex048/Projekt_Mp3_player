import menu
import song
import tkinter as tk
import buttons


application=menu.Menu()
application.printMenu()


x=application.start_thread(application.get_function_thread)
x.start()



while application.is_active:
    application.check_for_passable_input()
    application.do_command(application.get_input())   
print("koniec")