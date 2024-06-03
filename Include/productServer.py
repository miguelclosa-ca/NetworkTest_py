import socket
from product import Product


def initalizeProducts():
    """ Create a store's inventory.

    :return:
        An example of a store's inventory in list form.
    """
    products = []

    prod1 = Product(15.00, "category a", "name1")
    prod2 = Product(30.00, "category b", "name2")

    products.append(prod1)
    products.append(prod2)

    return products


# initalizeProducts()


def isCommand(message: str, store: list[Product]) -> bool:
    """ Check if a string of text is a boolean.
    :param message:
            Some message sent in from the client
    :return:
            bool: Whether if it was a command (True) or not (False)
    """
    validCommands = ["edit", "view", "quit"]

    # Here this checks if the first character of the message is a slash and if the word after it is contained in the
    # list of valid commands above.

    # TODO: there is definitely a way to find the longest value in a list in a short number of lines,
    #  add that value into the if statement
    if message[0] == "/" and message[1:5] in validCommands:
        if message[1:5] == validCommands[0]:
            editItems(message, store)
        elif message[1:5] == validCommands[1]:
            viewItems(message, store)

        return True

    else:
        return False


# isCommand()


def viewItems(message: str, items: list[Product]):

    splitCommand = message.split()
    print(splitCommand)

    for i in range(len(items)):
        if items[i].name == splitCommand[1]:
            print(items[i].toString())




def editItems(message: str, items: list[Product]):
    """
        With a /edit command, edit the parameters of some product.
        an example of a /edit would look like:
        /edit someProductName someProductAttribute someValue

    :param message:
        Given edit command to examine
    :param items:
    :return:
    """

    # Split the /edit command. This will make it easier to examine the command
    splitCommand = message.split()

    # Check if the /edit command is properly formed. That is, if the length of the command is equal to 4 "words"
    # If not, return false.
    if len(splitCommand) == 4:
        print(splitCommand)

        # Generate a list of the names of products in the store
        validProducts = []
        for i in range(len(items)):
            validProducts.append(items[i].name)

        print(validProducts)

        # Generate a list of valid attributes to examine
        # To do this, take the first item in the list of products and put all of its attributes into a list.
        validAttributes = []
        print(items[0].__dict__)
        for key, value in items[0].__dict__.items():
            validAttributes.append(key)
        print(validAttributes)


        # Assuming the command passes this if statement,
        # Change the attribute's variable
        if splitCommand[1] in validProducts and splitCommand[2] in validAttributes:
            for i in range(len(items)):
                if splitCommand[1] == items[i].name:

                    # TODO find a way to read the attributes
                    items[i].splitCommand[1] = splitCommand[3]

        else:
            return False
    else:
        print("no")






def main():
    # Create the list of products in the store
    productsInStore = initalizeProducts()

    while True:
        str = input("Enter command: ")

        if not isCommand(str, productsInStore):
            break


main()
