import hashlib

# Specify the filename of the image in the BLOCKCHAIN folder
filename = "C:/Users/Ashish Gupta/Desktop/Block chain/image1.jpeg"  # Update with your actual file name and path

# Read the image file in binary mode
with open(filename, 'rb') as f:
    # Read the file data
    file_data = f.read()

    # Calculate the SHA-256 hash of the file data
    image_hash = hashlib.sha256(file_data).hexdigest()

# Print the hashed code of the image
print("Hashed code of the image:", image_hash)