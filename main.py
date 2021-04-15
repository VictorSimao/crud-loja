import sys

from src.controller.functions import Functions

class Main:


    def __init__(self):
        self.functions = Functions()

        while True:
            self.get_user_input()


    def get_user_input(self):
        get_choice = self.functions.show_options()
        choice = get_choice
        self.get_choice(choice)


    def get_choice(self, choice):
        if choice == "a":
            self.functions.show_all_products()
            
        elif choice == "b":
            self.functions.create_product()
        
        elif choice == "c":
            self.functions.edit_product()
    
        elif choice == "d":
            self.functions.delete_product()
        
        elif choice == "e":
            self.functions.show_all_categories()
            
        elif choice == "f":
            self.functions.create_category()
        
        elif choice == "g":
            pass           
           
        elif choice == "h":
            self.functions.delete_category()
            
        elif choice == "i":
            sys.exit(1)

        else:
            print("Opção inválida")
            self.get_user_input()


Main()