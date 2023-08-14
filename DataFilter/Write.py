# export data
import xlsxwriter

import Global

def writeExcel(attri_list, data):
    
    Global.pro_file_path = Global.folder_path + "/" + "pro_" + Global.file_name + ".xlsx"

    book = xlsxwriter.Workbook(Global.pro_file_path)
    sheet = book.add_worksheet(Global.file_name)
    

    for row in range(len(data)+1):
        for col in range(len(data[0])):

            if(row == 0):
                sheet.write(row, col, attri_list[col])
                continue
            
            sheet.write(row, col, data[row-1][col])

    book.close()