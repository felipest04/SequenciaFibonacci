for _ in range(10):
    print(x >> 32)
    x = ((x & 0xffffffff) << 32) | ((x >> 32) + (x & 0xffffffff))
