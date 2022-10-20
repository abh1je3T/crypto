def encVigenere(msg, key):
    msg = msg.upper()
    key = key.upper()
    enc_txt = ""
    if len(msg) == len(key):
        for i in range(len(msg)):
            enc_num = ((ord(msg[i]) + ord(key[i])) % 26)
            enc_txt += chr(enc_num + 65)
    return enc_txt


def decVigenere(encMsg, key):
    encMsg=encMsg.upper()
    key=key.upper()
    if len(encMsg) == len(key):
        dec_txt = ""
        for i in range(len(encMsg)):
            dec_num = ((ord(encMsg[i]) - ord(key[i]) + 26) % 26)
            dec_txt += chr(dec_num + 65)
    return dec_txt


msg = "AbhijeetNaikwadi"
key = "NaikwadiAbhijeet"
enc_msg=encVigenere(msg,key)
print(enc_msg)
print(decVigenere(enc_msg,key))

