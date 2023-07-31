import os

from flat import Bill,Flatmate
from report import PDFReport


# 数据输入
amount = eval(input('输入房租费用：'))
period = input('输入房租日期：')
my_bill = Bill(amount, period)

name = input('输入住户姓名：')
days = int(input(f'输入{name}住宿时间：'))
flatmate1 = Flatmate(name, days)

name = input('输入住户姓名：')
days = int(input(f'输入{name}住宿时间：'))
flatmate2 = Flatmate(name, days)

print(f'{flatmate1.name}缴纳的房租为{flatmate1.pays(my_bill, flatmate2)}')
print(f'{flatmate2.name}缴纳的房租为{flatmate2.pays(my_bill, flatmate1)}')

pdf_report = PDFReport(f'{my_bill.period}.pdf')
pdf_report.generate(flatmate1, flatmate2, my_bill)


