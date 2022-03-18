# Below application is used to demonstrates operations on Excel file using xlsxwriter.
import os
import fnmatch
from sys import *
import xlsxwriter

def ExcelCreate(name):
    workbook = xlsxwriter.Workbook(name)

    worksheet = workbook.add_worksheet()

    worksheet.write('A1','Name')
    worksheet.write('B1', 'College')
    worksheet.write('C1', 'Mail ID')
    worksheet.write('D1', 'Mobile')

    workbook.close()

def main():
    print("-------Python Automation Scripts by Ashwini Raykar-------- ")
    print("Name of Application:", argv[0])

    if (len(argv) <2):
        print("Invalid Number of arguments")
        exit()

    if (argv[1] == '-u') or (argv[1] == '-U'):
        print("Help:ApplicationName Name_Of_File")
        exit()

    if (argv[1] == '-h') or (argv[1] == '-H'):
        print("Usage:This scripts is used to create excel file and write data into it")
        exit()

    try:
        ExcelCreate(argv[1])

    except Exception:
        print("Error:Invalid input")


if __name__ == "__main__":
    main()