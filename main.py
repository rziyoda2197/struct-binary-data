import struct

def int_to_binary(n):
    return struct.pack('i', n)

def float_to_binary(f):
    return struct.pack('f', f)

def string_to_binary(s):
    return struct.pack('1024s', s.encode())

def binary_to_int(b):
    return struct.unpack('i', b)[0]

def binary_to_float(b):
    return struct.unpack('f', b)[0]

def binary_to_string(b):
    return struct.unpack('1024s', b)[0].decode()

# Test qilish
n = 12345
f = 3.14159
s = "Hello, World!"

binary_n = int_to_binary(n)
binary_f = float_to_binary(f)
binary_s = string_to_binary(s)

print(f"Int {n} binary formati: {binary_n}")
print(f"Float {f} binary formati: {binary_f}")
print(f"String {s} binary formati: {binary_s}")

print(f"Binary formatdan int olingan: {binary_to_int(binary_n)}")
print(f"Binary formatdan float olingan: {binary_to_float(binary_f)}")
print(f"Binary formatdan string olingan: {binary_to_string(binary_s)}")
