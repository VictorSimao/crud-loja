from src.views.console.view_menu import ViewMenu

class Main:

    def __init__(self):
        self.console = ViewMenu()
        self.console.execute()

Main()
