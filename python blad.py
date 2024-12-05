# import cv2
# def compress_string(input_string):
#     if not input_string:
#         return ""
#
#     compressed = []
#     current_char = input_string[0]
#     count = 1
#
#     for char in input_string[1:]:
#         if char == current_char:
#             count += 1
#         else:
#             compressed.append(f"{count}{current_char}")
#             current_char = char
#             count = 1
#
#     compressed.append(f"{count}{current_char}")
#
#     return "".join(compressed)
#
# def comp_img(path):
#     img = cv2.imread(path)
#
#     pixel_data = img.flatten()
#
#     compressed = compress_string(pixel_data)
#
#     return compressed
#
# img_lol = r"C:\Users\basel.abdella\Desktop\lol"
# final = comp_img(img_lol)



# def compress_str(input_str):
#     compress = []
#     current_char = input_str[0]
#     count = 1
#
#     for char in input_str[1:]:
#         if char == current_char:
#             count += 1
#         else :
#             compress.append(f"{count}{current_char}")
#             current_char = char
#             count = 1
#
#     compress.append(f"{count}{current_char}")
#
#     return "".join(compress)
#
# x = input()
# out = compress_str(x)
# print(out)









# def re_decode(data):
#     decoded=""
#     count=""
#
#     for char in data:
#         if char.isdigit():
#             count += char
#         else:
#             decoded += char * int(count)
#             count=""
#
#
#     return decoded
#
#
# compressed_text = input()
# output = re_decode(compressed_text)
# print(output)
#
#
#
#





