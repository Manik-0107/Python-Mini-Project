# import the modules
from PyPDF2 import PdfReader
import pyttsx3

# Open the PDF file
path = r'C:\Users\Manik0107\Downloads\Documents\Unit-1.pdf'
pdfReader = PdfReader(path)

# Get an engine instance for speech synthesis
speak = pyttsx3.init()

# Loop through all pages
for page in pdfReader.pages:
    text = page.extract_text()
    if text:  # Only speak if there is text
        speak.say(text)
        speak.runAndWait()

speak.stop()
