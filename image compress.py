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


def comp_img(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale for simplicity
    if img is None:
        raise ValueError("Image not found or unable to load.")

    pixel_data = img.flatten()
    compressed = run_length_encode(pixel_data)
    return compressed


def reconstruct_img(compressed_data, original_shape):
    decompressed_data = run_length_decode(compressed_data)
    return np.array(decompressed_data, dtype=np.uint8).reshape(original_shape)


# Example usage
img_path = r"C:\Users\basel.abdella\Desktop\lol.bmp"
compressed = comp_img(img_path)

# Load original image to get its shape
original_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
if original_img is not None:
    reconstructed_img = reconstruct_img(compressed, original_img.shape)
    output_path = r"C:\Users\basel.abdella\Desktop\reconstructed_lol.bmp"
    cv2.imwrite(output_path, reconstructed_img)
    print(f"Image compressed and saved successfully at: {output_path}")
else:
    print("Error in loading the original image for shape reference")
