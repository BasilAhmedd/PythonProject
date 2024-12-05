import cv2
import numpy as np


def run_length_encode(data):
    compressed = []
    current_value = data[0]
    count = 1

    for value in data[1:]:
        if value == current_value:
            count += 1
        else:
            compressed.append((current_value, count))
            current_value = value
            count = 1

    compressed.append((current_value, count))
    return compressed


def run_length_decode(compressed_data):
    decompressed = []
    for value, count in compressed_data:
        decompressed.extend([value] * count)
    return decompressed


def resize_for_compression(image, scale_percent=50):
    # Resize the image by the specified scale percentage
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized_image


def comp_img(path, scale_percent=50):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Image not found or unable to load.")

    # Resize image
    resized_img = resize_for_compression(img, scale_percent)

    pixel_data = resized_img.flatten()
    compressed = run_length_encode(pixel_data)
    return compressed, resized_img.shape


def reconstruct_img(compressed_data, original_shape):
    decompressed_data = run_length_decode(compressed_data)
    return np.array(decompressed_data, dtype=np.uint8).reshape(original_shape)


# Paths
original_img_path = r"C:\Users\basel.abdella\Desktop\lol.bmp"
compressed_img_path = r"C:\Users\basel.abdella\Desktop\compressed_lol.bmp"

# Compress the image
scale_percent = 50  # Resize to 50% of the original dimensions for compression
compressed, resized_shape = comp_img(original_img_path, scale_percent)

# Reconstruct the image from the compressed data
reconstructed_img = reconstruct_img(compressed, resized_shape)

# Save the reconstructed (compressed) image
cv2.imwrite(compressed_img_path, reconstructed_img)

# Display the original and reconstructed images
original_img = cv2.imread(original_img_path, cv2.IMREAD_GRAYSCALE)

cv2.imshow('Original Image', original_img)
cv2.imshow('Compressed Image', reconstructed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Compressed image saved successfully at: {compressed_img_path}")
