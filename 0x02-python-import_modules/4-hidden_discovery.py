# !/usr/bin/python3

# import struct


# if __name__ == "__main__":
#     """Print all names defined by hidden_4 module."""
#     import hidden_4

#     names = dir(hidden_4)
#     print(names)


#     with open('hidden_4.pyc', 'rb') as f:
#         print struct.unpack('<H', f.read(2))

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
