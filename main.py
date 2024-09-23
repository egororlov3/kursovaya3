from utilits import open_file, get_executed_operations, sort_operations, format_operation, print_operations

if __name__ == "__main__":
    data = open_file()
    executed_operations = get_executed_operations(data)
    last_five_operations = sort_operations(executed_operations)
    format_operation(last_five_operations)
    print_operations(last_five_operations)


