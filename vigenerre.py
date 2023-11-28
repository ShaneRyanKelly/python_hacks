def generate_cypher(string):
    cypher = [None] * (len(string)) 
    for i in range(len(string)):
        offset = (ord(string[i].lower()) - 97)
        cypher[i] = offset
    return cypher

def encrypt(string, cypher):
    encrypted = [None] * (len(string)) 
    cypher_index = 0
    for i in range(len(string)):
        if cypher_index >= len(cypher):
            cypher_index = 0
        if ord(string[i].lower()) > 122 or ord(string[i].lower()) < 61: 
            encrypted[i] = string[i]
            continue
        offset = ord(string[i].lower()) + cypher[cypher_index]
        if (offset > 122):
            offset -= 26
        encrypted[i] = chr(offset)
        cypher_index += 1
    return encrypted

def print_code(string):
    code = ""
    for i in range(len(string)):
        code += string[i]
    print(code)

def main():
    plaintext = input("Enter a string to encrypt: ")
    cypher_string = input("Enter a cypher: ")
    cypher = generate_cypher(cypher_string)
    encrypt_text = encrypt(plaintext, cypher)
    print_code(encrypt_text)

main()