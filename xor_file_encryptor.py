def xor_encrypt(data, key):
    # Encrpyting using XOR and the key provided
    data = bytearray(data) # Converting the byte string to a byte array

    '''
    Enumerate function takes in an array as input and 
    gives a list as the output which contains tuples in the
    key-value pair with index of array as key and value at the index as value
    '''
    for index, value in enumerate(data):
        data[index] = value ^ int(key)

    return data.decode()

def xor_decrypt(data, key):
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ int(key)
    return data.decode()
