from PIL import Image

def identify_color_change(image_path1, image_path2, output_path):
    # Read the images
    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)

    # Ensure both images have the same size
    if img1.size != img2.size:
        raise ValueError("Images must have the same size for comparison.")

    # Create an empty image to visualize color changes
    color_change_img = Image.new("RGB", img1.size)

    # Threshold for detecting color change
    threshold = 50

    # Iterate through pixels to identify color changes
    for x in range(img1.width):
        for y in range(img1.height):
            pixel1 = img1.getpixel((x, y))
            pixel2 = img2.getpixel((x, y))

            # Calculate the absolute difference in RGB values
            diff = sum(abs(c1 - c2) for c1, c2 in zip(pixel1, pixel2))

            # Check if the difference exceeds the threshold
            if diff > threshold:
                # If a color change is detected, mark the pixel as red in the result image
                color_change_img.putpixel((x, y), (255, 0, 0))

    # Display the original images and the image highlighting color changes
    img1.show(title='Image 1')
    img2.show(title='Image 2')
    color_change_img.show(title='Color Changes')

    # Save the result image
    color_change_img.save(output_path)

if __name__ == "__main__":
    image_path1 = "red.jpg"
    image_path2 = "orange.png"
    output_path = "Color-blue.jpg"

    identify_color_change(image_path1, image_path2, output_path)
