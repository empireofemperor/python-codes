# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
  


# String which represents the QR code 

s = input("QR code Creater.\nEnter the url to create the QR-CODE.\n\nURl : ")
  
# Generate QR code 
url = pyqrcode.create(s)

print('Url is getting genrated.')
print('Url is getting genrated..')
print('Url is getting genrated...')
print('Url is getting genrated....')
print('Url is getting genrated.....\n')
print('URL genrated sucessfully...:)')
  
# Create and show" 
url.show()
