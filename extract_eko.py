from PyPDF2 import PdfFileReader

pdfFileObj = open('Ekofisk.pdf','rb')
input1 = PdfFileReader(pdfFileObj, strict=False)
num_p = input1.getNumPages()

found = False
page_num = 0
for n in range(0, num_p):
    p = input1.getPage(n)
    p_text= p.extractText().lower()
    p_text = p_text.split('\n')
    for i, v in enumerate(p_text):
        if 'all year waves' in v:
            found = True
            page_num = n
            break

text = input1.getPage(page_num).extractText().lower()
text = text.split('\n')
value1 = []
index1 = 0
value2 = []
stop = False
output = dict()
candidates = None
for i, t in enumerate(text):
    if t.startswith('significant wave height hs m'):
        candidate_list = t.split()
        candidates = [c for c in candidate_list if c.isalpha()==False]
        value1 = candidates[:3]
        index1 = i

for j in range(index1, len(text)):
    if text[j].startswith('peak period'):
        candidate_list = text[j+1].split()
        candidates = [c for c in candidate_list if c.isalpha()==False]
        value2 = candidates[:3]

out_list = list(zip(value1, value2))
output['1'] = out_list[0]
output['10'] = out_list[1]
output['100'] = out_list[2]

if __name__ == '__main__':
    print(output)
