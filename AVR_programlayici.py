import os




mod = input("YAZILACAK MI OKUNACAK MI ? : syntax w/r \n")

if(mod == "r"):
    konum="source.hex"


else:
    konum = input("konumu giriniz : \n ")


S = "avrdude -c arduino -P COM7 -b 115200 -p m328p -U flash:" +mod + ":" + konum +":i"


os.system(S)  # returns the exit code in unix
print('HEX kodu atıldı\n ')



input("kapatmak için enter tıkla")


