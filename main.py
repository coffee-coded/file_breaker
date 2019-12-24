from breaker import aes

if __name__ == '__main__':
    aes = aes()
    file = input("File : ")
    i = int(input("1. Encrypt \n2. Decrypt \nChoose : "))
    if i == 1:
        aes.encrypt_file(file)
    else:
        aes.decrypt_file(file)
