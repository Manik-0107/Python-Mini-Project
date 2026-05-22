from captcha.image import ImageCaptcha
from PIL import Image
import random
import string

# Configuration
WIDTH, HEIGHT = 350, 120
DIFFICULTY = "medium"       # easy, medium, hard

def generate_captcha_text(length=6):
    """Generate random text for CAPTCHA"""
    chars = string.ascii_uppercase + string.digits
    # Remove confusing characters
    chars = chars.replace('0', '').replace('1', '').replace('I', '')
    return ''.join(random.choices(chars, k=length))

# Create Image
image = ImageCaptcha(width=WIDTH, height=HEIGHT)

# Generate Random Text or use custom input
choice = input("Generate random CAPTCHA? (y/n): ").lower()
if choice == 'y':
    captcha_text = generate_captcha_text()
    print(f"Generate text: {captcha_text}")
else:
    captcha_text = input("Enter captcha text (max 8 chars): ").upper()[:8]

# Generate and save
filename = f"CAPTCHA_{captcha_text}.png"
image.write(captcha_text, filename)

# Display
Image.open(filename).show()

# Verification
user_input = input("\nEnter the character you see: ")
if user_input.upper() == captcha_text:
    print("Correct")
else:
    print(f"Incorrect! The text was: {captcha_text}")


# First install: pip install captcha
