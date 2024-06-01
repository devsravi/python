import random
import os
import qrcode

# Ask user for file name
name = input("Enter your file name: ")

# Generate random number
randomNumber = random.randint(1000, 9999)

# Determine the Downloads directory path based on the operating system
home = os.path.expanduser("~")
if os.name == 'nt':  # Windows
    downloads_directory = os.path.join(home, "Downloads")
else:  # macOS and Linux
    downloads_directory = os.path.join(home, "Downloads")

# Ensure the directory exists
if not os.path.exists(downloads_directory):
    os.makedirs(downloads_directory)

# Construct the full path for the file
fileName = os.path.join(downloads_directory, name + str(randomNumber) + ".png")

# Ask user for data to encode in QR code
user_input = input("Enter the data for the QR code: ")

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,
    border=4,
)

qr.add_data(user_input)
qr.make(fit=True)

# Generate image with specified colors
img = qr.make_image(fill_color="red", back_color="white")

# Save the image to the specified directory
img.save(fileName)

print(f"QR code saved as {fileName}")
