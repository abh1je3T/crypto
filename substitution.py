def encSubtitution(msg, key):
    enc_txt = ""
    for i in msg:
        enc_num = ((ord(i) - 65) + key) % 26
        enc_txt += chr(enc_num + 65)
    return enc_txt


def decSubstitution(encMsg, key):
    dec_txt = ""
    for i in encMsg:
        dec_num = ((ord(i) - 65) - key) % 26
        dec_txt += chr(dec_num + 65)
    return dec_txt


msg = "AbhijeetNaikwadi"
toUpper = msg.upper()
key = 5
enc = encSubtitution(toUpper, key)
print(enc)
print(decSubstitution(enc, key))
