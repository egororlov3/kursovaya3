import json
from utilits import open_file, get_executed_operations, sort_operations

operations = open_file()
executed_operations = get_executed_operations(operations)
sorted_operations = sort_operations(executed_operations)

#пройти в цикле по последним пяти операциям и напечатать каждую

print(operations)





