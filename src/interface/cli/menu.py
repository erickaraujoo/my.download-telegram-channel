from InquirerPy import inquirer
from InquirerPy.utils import InquirerPyListChoices


def show_menu(choices: InquirerPyListChoices, message: str):
    option = inquirer.select(message=message, choices=choices).execute()

    return option
