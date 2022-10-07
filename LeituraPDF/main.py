import PyPDF2
import re
import os

print(os.listdir('./pdfs'))

lista_arquivos = os.listdir('./pdfs')
caminho = 'C:\\Users\\Danie\\Desktop\\Python\\LeituraPDF\\pdfs\\'

for pdf in lista_arquivos:
    with open(caminho + pdf, 'rb') as pdf_file:
        dados = PyPDF2.PdfFileReader(pdf_file)
        pagina = dados.getPage(0)
        r = re.search(r"\d{8,8}",str(pagina.extractText())).group()
    print(pdf,'--', r)
    os.rename(caminho+pdf, caminho+r+'.pdf')
