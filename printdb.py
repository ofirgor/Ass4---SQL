from persistence import *

def main():
    #TODO: implement
    tables_names = {k: v for k, v in repo.__dict__.items() if isinstance(v, Dao)}
    for table in sorted(tables_names):
        table_name = table.capitalize()
        table_data = repo.execute_command('SELECT * FROM {}'.format(table))
        print(table_name)
        # decode the binary strings in the second column
        table_data = [[val.decode() if isinstance(val, bytes) else val for val in row] for row in table_data]
        for row in table_data:
            print(tuple(row))


if __name__ == '__main__':
    main()