try:
    path = input(r"Enter path of your Image: ")

    key= int(input("Enter key for encryption of Image: "))

    print("The path of file: ", path)
    print("Nte: Encryption key and Decryption key must be same.")
    print("Key for decryption: ")

    fin = open(path, 'rb')

    image = fin.read()
    fin.close

    image = bytearray(image)

    for index, values in enumerate(image):
       image[index] = values ^ key

    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    print("Encryption Done! ")
       

except Exception:
    print("Error caught: ", Exception._name_)
