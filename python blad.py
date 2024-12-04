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
#
# input_text = input()
# output = compress_string(input_text)
# print(output)


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




#
# import re
#
#
# def decompress_string(compressed_string):
#     matches = re.findall(r'(\d+)([A-Za-z])', compressed_string)
#     decompressed = []
#
#     for count, char in matches:
#         decompressed.append(char * int(count))
#
#     return "".join(decompressed)
#
#
#
# compressed_text = input()
# output = decompress_string(compressed_text)
# print(output)


# import re
#
#
# def decompress_string(compressed_string):
#     matches = re.findall(r'(\d+)([A-Za-z])', compressed_string)
#     decompressed = []
#
#     for count, char in matches:
#         decompressed.append(char * int(count))
#
#     return "".join(decompressed)
#
#
#
# compressed_text = input()
# output = decompress_string(compressed_text)
# print(output)

def re_decode(data):
    decoded=""
    count=""

    for char in data:
        if char.isdigit():
            count += char
        else:
            decoded += char * int(count)
            count=""


    return decoded


compressed_text = input()
output = re_decode(compressed_text)
print(output)







