# Command to install dependencies:
# pip3 install camelot-py[cv]

# Ghostscript
# https://ghostscript.com/releases/gsdnld.html

import camelot
# import os

# change working directory
# os.chdir("")

file = "table_1.pdf"

# extract all the tables in the PDF file
tables = camelot.read_pdf(file)

# number of tables extracted
print("Total tables extracted:", tables.n)

# print the first table as Pandas DataFrame
print(tables[0].df)

# export the list of tables as CSV
tables.export("res.csv", f="csv", compress=False)