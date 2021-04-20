from src.views.console.view_menu import ViewMenu

class Main:

    @staticmethod
    def run():
        console = ViewMenu()
        console.execute()


Main.run()
