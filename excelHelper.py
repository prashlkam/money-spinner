
# Writing to an excel sheet using Python
import xlwt
import tick
import xlrd

# ticks = tick.ticks(60, 85.5, 92.7)
cellrange = [[7, 3], [65527, 63]]
sh1 = 'ongc eq ticks'
fil1 = './data/ongc eq ticks 01.xlsx'

def writetoExcel(data, sheetname, file):
    # Workbook is created
    wb = xlwt.Workbook()
    # add_sheet is used to create sheet.
    if sheetname == '':
        sheetname = 'Sheet 1'
    sheet1 = wb.add_sheet(sheetname)
    # positioning for writing data in excel sheet
    r = 7
    c = 3
    # write data to sheet
    # write title
    title = sheetname.upper()
    sheet1.write(1, 5, title)
    # write column headings
    for i in range(len(data)):  # rows
        sheet1.write(r - 2, c + i, 'Sec ' + str(i + 1))
    for i in range(len(data)): # rows
        for j in range(len(data[i])): # cols
            if j > 65520:
                continue
            sheet1.write(r + j, c + i, data[i][j])
    # save workbook
    wb.save(file)

def readFromExcel(file, sheetname, rangeofcells):
    loc = (file)
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_name(sheetname)
    ticks = []
    # t = []
    print(rangeofcells)
    # range is of the form [[row1, col1], [rown, coln]]
    for i in range(rangeofcells[0][1], rangeofcells[1][1]): # cols
        t = []
        for j in range(rangeofcells[0][0], rangeofcells[1][0]): # rows
            t.append(sheet.cell_value(j, i))
        ticks.append(t)
    return ticks

# writetoExcel(ticks, sh1, fil1)
res = readFromExcel(fil1, sh1, cellrange)
print('No. of Secs: ', len(res))
print('No. of Ticks per Second: ', len(res[0]))
