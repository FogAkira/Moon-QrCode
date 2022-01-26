import os
os.system("pip install -r requirements.txt")
import qrcode
import cv2
system = input("Are You In Windows? y/n :")

if system == "y":
 open_website = "start https://dev--moonportfolio.fogakira.autocode.gg/"
 system_clear = "cls"
 os.system("cls")

elif system == "n":
 open_website = "xdg-open \"\" https://dev--moonportfolio.fogakira.autocode.gg/"
 system_clear = "clear"
 os.system("clear")

def restart():
    input("Press Enter To Continue")
    os.system("python main.py")

print("""

$$\      $$\                               
$$$\    $$$ |                              
$$$$\  $$$$ | $$$$$$\   $$$$$$\  $$$$$$$\  
$$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$  __$$\ 
$$ \$$$  $$ |$$ /  $$ |$$ /  $$ |$$ |  $$ |
$$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
$$ | \_/ $$ |\$$$$$$  |\$$$$$$  |$$ |  $$ |
\__|     \__| \______/  \______/ \__|  \__|

               Welcome to Moon QrCode Genretor And Decoder

               Made By Moon?#2997                            

        1 = Generator                2 = Decoder   
        0 = exit                     3 = Moon Website     
""")

menu_selected = input("Selected : ")

if menu_selected == "0":
    os.system(system_clear)
    print("GoodBye!")

elif menu_selected == "1":
 qr_code_content = input("Text Or Link : ")
 qr_code_img_name = input("File Name : ")
 img = qrcode.make("" + qr_code_content + "")
 img.save("" + qr_code_img_name + ".jpg")
 print("Done, Now Open The Folder And Browse For " + qr_code_img_name + ".jpg")
 restart()

elif menu_selected == "2":
    file_name = input("File Name : ")
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("" + file_name + ".jpg"))
print("QRCode Text Is : ", val)
restart()

if menu_selected == "3":
 os.system(open_website)

else:
 restart()