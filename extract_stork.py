from PyPDF2 import PdfFileReader

pdfFileObj = open('Storklakken.pdf','rb')
input1 = PdfFileReader(pdfFileObj, strict=False)
num_p = input1.getNumPages()

found = False
page_num = 0
for n in range(4, num_p):
    p = input1.getPage(n)
    p_text= p.extractText().lower()
    p_text = p_text.split('\n')
    for i, v in enumerate(p_text):
        if 'wave and current data' in v:
            found = True
            page_num = n
            break

text = input1.getPage(page_num).extractText().lower()
text = text.split('\n')

value1 = []
value2 = []
output = dict()
for i, t in enumerate(text):
    if t.startswith(' 0.63'):
        value1.append(text[i+1].split()[-1])
        value2.append(text[i+3].split()[-1])
    elif t.startswith(' 10-1'):
        value1.append(t.split()[-1])
        value2.append(text[i+2].split()[-1])
    elif t.startswith(' 10-2'):
        value1.append(t.split()[-1])
        value2.append(text[i+2].split()[-1])
        break

out_list = list(zip(value1, value2))
output['1'] = out_list[0]
output['10'] = out_list[1]
output['100'] = out_list[2]

if __name__ == '__main__':
    print(output)
