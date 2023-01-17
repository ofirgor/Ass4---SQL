from persistence import *

import sys


def update_quantity(splittedline: list[str], is_sale):
    id_product = int(splittedline[0])
    quantity_action = int(splittedline[1])
    curr_quantity = repo.products.find(id=id_product)[0].quantity
    if is_sale and curr_quantity < quantity_action:
        return
    new_quantity = curr_quantity + quantity_action
    repo.products.update("quantity", new_quantity, id_product)


def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            # add to quantity table
            quantity = int(splittedline[1])
            is_sale = quantity < 0
            update_quantity(splittedline, is_sale)



            #TODO: apply the action (and insert to the table) if possible


if __name__ == '__main__':
    main(sys.argv)
