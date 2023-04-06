msg = '1101101 1100110 1110001 1110001 1110100'


decoded_msg = ''
binary_list = msg.split(' ')
for bin_num in binary_list:
    integer = int(bin_num, 2) - 5
    letter = chr(integer)
    decoded_msg += letter
print(decoded_msg)