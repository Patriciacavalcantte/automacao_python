import PyPDF2
import os
"""
Essas linhas importam os módulos necessários. PyPDF2 é uma biblioteca em 
para trabalhar com arquivos PDF, 
e OS fornece funções para interagir com o sistema operacional.
"""


merger = PyPDF2.PdfMerger() #uma instância da classe PdfMerger da biblioteca PyPDF2 é criada. Esse objeto será usado para mesclar vários arquivos PDF juntos.
lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort() #é chamado  para ordenar o conteúdo em ordem alfabética.
print(lista_arquivos)

for arquivo in lista_arquivos:
    if".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")

merger.write("PDF_final.pdf")