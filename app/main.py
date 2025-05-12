import qrcode
import os

def generate_qr_code():
    # Create images directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')

    # Get the URL from the user
    url = input("Enter the URL to encode: ")
    name = input("Enter the name of the QR code: ")

    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add the URL to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color='black', back_color='white')

    # Save the image in the images directory
    img_path = os.path.join('images', f"{name}.png")
    img.save(img_path)

    print(f"QR code saved as {img_path}")

if __name__ == "__main__":
    generate_qr_code()