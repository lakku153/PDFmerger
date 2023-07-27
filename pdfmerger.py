import PyPDF2
pdffiles=['a.pdf','b.pdf','c.pdf']
merge=PyPDF2.PdfMerger()
for filename in pdffiles:
    pdfiles=open(filename,'rb')
    pdfreader=PyPDF2.PdfReader(pdfiles)
    merge.append(pdfreader)
pdfiles.close()
merge.write('merged.pdf')