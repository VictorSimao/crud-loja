from src.view.console.view_menu import ViewMenu

from settings import init_db


init_db()
console = ViewMenu()
console.execute()
