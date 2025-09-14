import sys

if len(sys.argv) < 2: 
  print("Usage: python script.py <number1> <number2>") 
  sys.exit(1)

script_name = sys.argv[1]

from prettytable import TableStyle, from_csv
with open(f"{script_name}.csv") as fp:
    table = from_csv(fp)
    table.set_style(TableStyle.MARKDOWN)
print(table.get_string(sortby="Ističe"))
