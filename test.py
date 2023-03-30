from openpyxl import Workbook
import os

excelPath = os.getcwd()


resultWorkBook = Workbook(excelPath)
sheet = resultWorkBook.create_sheet('sheet1')

alist=[ '其它电容 Other Capacitor', ['铝电解电容', '100uF', '±20%', '16V', '6.3*5.7mm'],'VEJ101M1CTR-0605']
# sheet.append(alist)

resultWorkBook.save("Tst.xlsx")
print(alist)
blist = ["1","A"]
print(blist)
alist[2:2]=blist
print(alist)

