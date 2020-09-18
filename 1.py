string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
for i in string:
    if ord(i)<=122 and ord(i)>=97:
        if ord(i)+2>122:
            print(chr(ord(i)+2-26),end="")
        else:
            print(chr(ord(i)+2),end="")
    else:
        print(i,end="")
#apply it on url
#answer = ocr
