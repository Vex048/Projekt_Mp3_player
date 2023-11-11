import menu
import queue_1
application=menu.Menu()


while application.is_active:
    application.check_for_passable_input()
    application.do_command(application.get_input())
print("koniec")