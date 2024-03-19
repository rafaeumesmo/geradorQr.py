import qrcode
from PIL import Image
import tempfile
import webbrowser

texto = input("Digite o texto que você deseja codificar no QR code: ")
qr = qrcode.make(texto)
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
qr.save(temp_file.name)
webbrowser.open(temp_file.name)
temp_file.close()