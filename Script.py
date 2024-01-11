import img2pdf
from PIL import Image

#Syanx

img = "C:\\Users\\Strendev\\Strendev.png" # Image Path(Copy full image path) (Directory Path use \\ in case of error while useing \ )// 

pdf = "C:\\Users\\Strendev\\Strendev.pdf" # PDF Path (Directory Path use \\ in case of error while useing \ ) (In  case of Strendev.pdf you can give any name ad username.pdf)


image  = Image.open(img)

pdf_converted = img2pdf.convert(image.filename)

with open(pdf, "wb") as file:
    file.write(pdf_converted)

print("PDF Created Successfully ")
print("# Subscribe to Strendev # https://www.youtube.com/@Strendev # ")
