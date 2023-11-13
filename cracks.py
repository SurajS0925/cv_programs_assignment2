from PIL import Image, ImageFilter

def identify_cracks(image_path):
    # Read the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_img = img.convert("L")

    # Apply an edge filter
    edges = grayscale_img.filter(ImageFilter.FIND_EDGES)

    # Display the original and processed images
    img.show(title='Original Image')
    edges.show(title='Identified Cracks')

if __name__ == "__main__":
    image_path = "crack.jpeg"
    identify_cracks(image_path)