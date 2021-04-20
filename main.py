from src.views.web.start import app
from src.views.console.view_menu import ViewMenu

class Main:

    @staticmethod
    def run():
        # console = ViewMenu()
        # console.execute()
        app.run(debug=True)
        
Main.run()