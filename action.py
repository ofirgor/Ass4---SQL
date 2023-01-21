from persistence import *

import sys


def update_quantity(splittedline, is_sale):
    product_id = int(splittedline[0])
    quantity_action = int(splittedline[1])
    curr_quantity = repo.products.find(id=product_id)[0].quantity
    if is_sale and curr_quantity < quantity_action:
        return
    dto_instance = Activitie(product_id, quantity_action, splittedline[2], splittedline[3])
    repo.activities.insert(dto_instance) # add action to the activities table
    new_quantity = curr_quantity + quantity_action
    repo.products.update_quantity(new_quantity, product_id)


def main(args):
    inputfilename = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline = line.strip().split(", ")
            quantity = int(splittedline[1])
            is_sale = quantity < 0
            update_quantity(splittedline, is_sale)



            #TODO: apply the action (and insert to the table) if possible


if __name__ == '__main__':
    main(sys.argv)
