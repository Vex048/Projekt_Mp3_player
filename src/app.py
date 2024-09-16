import sys
sys.path.insert(1, 'main/')
from gui import GUI
import globaly

globaly.init()
application=GUI()

if application.active==False:
    print("Koniec")
