# pip3 install tabula-py
import tabula
import os

# change working directory
os.chdir("C:\\Users\\Light\\Desktop\\extract tabular data from pdf\\tabula-py")

# read PDF file
tables = tabula.read_pdf("sample_4.pdf", pages="all")

# save them in a folder
folder_name = "tables"
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
# iterate over extracted tables and export as excel individually
for i, table in enumerate(tables, start=1):
    table.to_excel(os.path.join(folder_name, f"table_{i}.xlsx"), index=False)

# # convert all tables of a PDF file into a single CSV file
# # supported output_formats are "csv", "json" or "tsv"
# tabula.convert_into("1710.05006.pdf", "output.csv", output_format="csv", pages="all")

# # convert all PDFs in a folder into CSV format
# # `pdfs` folder should exist in the current directory
# tabula.convert_into_by_batch("pdfs", output_format="csv", pages="all")