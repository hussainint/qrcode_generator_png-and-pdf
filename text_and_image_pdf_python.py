import fpdf 
import pyqrcode

data="aajgvdksdcshdbckgsdvcdvckdvcvdvsdvsdv"

qr=pyqrcode.create(data)



qr.png("qrcodee.png", scale=8)



pdf = fpdf.FPDF(format='letter') #pdf format
pdf.add_page() #create new page
pdf.set_font("Arial", size=12) # font and textsize

data="line1\nline2\nline3\nline4"
k=data.split('\n')
for i in k:
	pdf.cell(200, 10, txt=i, ln=1, align="L")
pdf.image('qrcodee.png',w=50,h=50)
pdf.output("qrcodee.pdf")



