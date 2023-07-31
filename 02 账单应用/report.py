import webbrowser
import os
from fpdf import FPDF

absolute_path = os.path.abspath('.') + '/files'


# PDF报告
class PDFReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        pdf = FPDF(unit='pt', format='A4')
        pdf.add_page()
        pdf.set_font('Arial', size=24, style='B')
        pdf.image(f'{absolute_path}/bill.png', w=50, h=50)
        pdf.cell(0, 50, 'Bills', align='C', ln=1)

        pdf.set_font('Arial', size=14, style='B')
        pdf.cell(100, 50, 'Date', border=1, align='C')
        pdf.cell(150, 50, txt=bill.period, border=1, align='C', ln=1)

        pdf.set_font('Arial', size=12)
        pdf.cell(100, 50, txt=flatmate1.name, border=1, align='C')
        pdf.cell(150, 50, txt=flatmate1_pay, border=1, align='C', ln=1)

        pdf.cell(100, 50, txt=flatmate2.name, border=1, align='C')
        pdf.cell(150, 50, txt=flatmate2_pay, border=1, align='C', ln=1)
        pdf.output(f'{absolute_path}/{self.filename}')

        webbrowser.open(f'{absolute_path}/{self.filename}')
