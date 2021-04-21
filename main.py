from src.views.web.start import app


class Main:

    @staticmethod
    def run():
        # console = ViewMenu()
        # console.execute()
        app.run(debug=True)


Main.run()
