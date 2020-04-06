# with open("binary", 'bw') as bin_file: #'bw' means to write binary
#     for i in range(17):
#         bin_file.write(bytes([i])) #write() function writes the data, bytes() function converts integer into binary
#
# with open("binary", 'br') as binfi: #'br' means to read binary
#     for b in binfi:
#         print(b)
#         # Output:
#             # b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n'
#             # b'\x0b\x0c\r\x0e\x0f\x10'
#
#

a = 24873
b = 25534

with open("binary", 'bw') as bifi:
    bifi.write(a.to_bytes(2, 'big')) #It writes a into binary in the binary file
    bifi.write(b.to_bytes(2, 'big'))

with open("binary", 'br') as bific:
    c = int.from_bytes(bific.read(2), 'big') #It reads first binary number from the binary file,converts in int
    print(c) #and prints
    d = int.from_bytes(bific.read(2), 'big')
    print(d)

#Aajhai pani yesmaa maile line (18, 19, 22, 24) maa vaako (2, 'big') ko meaning tyakkai bujheko xaina hai guyz

