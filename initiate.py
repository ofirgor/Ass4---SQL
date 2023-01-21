from persistence import *

import sys
import os

def add_branche(splittedline):
    #TODO: add the branch into the repo
    dto_instance = Branche(splittedline[0], splittedline[1], splittedline[2])
    repo.branches.insert(dto_instance)


def add_supplier(splittedline):
    #TODO: insert the supplier into the repo
    dto_instance = Supplier(splittedline[0], splittedline[1], splittedline[2])
    repo.suppliers.insert(dto_instance)


def add_product(splittedline):
    #TODO: insert product
    dto_instance = Product(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
    repo.products.insert(dto_instance)


def add_employee(splittedline):
    #TODO: insert employee
    dto_instance = Employee(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
    repo.employees.insert(dto_instance)


adders = {"B": add_branche,
          "S": add_supplier,
          "P": add_product,
          "E": add_employee}


def main(args):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    # uncomment if needed
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])


if __name__ == '__main__':
    main(sys.argv)
