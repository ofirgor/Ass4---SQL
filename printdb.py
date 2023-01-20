from persistence import *

def main():
    # print all tables

    tables_names = {k: v for k, v in repo.__dict__.items() if isinstance(v, Dao)}
    for table in sorted(tables_names):
        table_name = table.capitalize()
        table_data = repo.execute_command('SELECT * FROM {}'.format(table))
        print(table_name)
        # decode the binary strings in the second column
        table_data = [[val.decode() if isinstance(val, bytes) else val for val in row] for row in table_data]
        for row in table_data:
            print(tuple(row))
    # print employees report

    print("Employees report")
    employees_data = repo.execute_command('SELECT employees.name, employees.salary, branches.location\
                                        , (SELECT SUM(-quantity* (SELECT price FROM products WHERE products.id = activities.product_id))\
                                        FROM activities WHERE activities.activator_id = employees.id)\
                                        as total_sales FROM employees JOIN branches ON employees.branche = branches.id')
    # decode the binary strings in the second column
    table_data = [[val.decode() if isinstance(val, bytes) else val for val in row] for row in employees_data]
    table_data = [[0 if val is None else val for val in row] for row in table_data]
    for row in sorted(table_data, key=lambda x: x[0]):
        print(" ".join([str(x) for x in row]))


if __name__ == '__main__':
    main()