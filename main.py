from src.views.console.view_menu import ViewMenu

class Main:

    def run(self):
        self.console = ViewMenu()
        self.console.execute()


main = Main()
main.run()
