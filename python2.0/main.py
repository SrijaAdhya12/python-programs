
#type python in terminal to run python interpreter
#type exit() to exit python interpreter
# python is dynamicly typed language, they can be reassigned, no data type is required to be specified

#Good coding practices
#define def main() -> None:
#if __name__ == '__main__':
#   main()

from module import connect

connect()

number: int = 10 #type annotation

def upper_everything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]

