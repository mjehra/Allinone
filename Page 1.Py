import requests
import os
from cfonts import render  

        
import webbrowser
webbrowser.open ('https://t.me/GODTEST')
from datetime import datetime
def check_date():
    current_date = datetime.now().date()
    target_date = datetime(2025, 2, 10)  .date()
    if current_date >= target_date:
        print('\n - New file in Server')
        webbrowser.open("https://t.me/GOTEST")
        exit()

check_date()  
      
ehra = render('PAGE [1]', colors=['cyan', 'white'], align='center')
print("\x1b[1;39m—" * 60)
print(ehra)
print("PROGRAMMER @MYEHRA |  Channel:  @GODTEST ")
print("\x1b[1;39m—" * 60)

webbrowser.open ('https://t.me/GODTEST')




print(f"""\x1b[38;5;117m  1\x1b[38;5;231m - INSTAGRAM [GMAIL]  \x1b[1;32m 
\x1b[38;5;117m◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
 2\x1b[38;5;231m - INSTAGRAM [G+H] \x1b[1;32m\x1b[1;32m 
\x1b[38;5;117m◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙\x1b[38;5;117m  3\x1b[38;5;231m - AOL INSTAGRAM  \x1b[1;32m
\x1b[38;5;117m◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
\x1b[38;5;117m  4\x1b[38;5;231m - CRUNCHYROLL [CHECKER 
\x1b[38;5;117m◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
\x1b[38;5;117m  5\x1b[38;5;231m - Facebook [Random] | \x1b[1;32m
\x1b[38;5;117m◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙ 
""")




def khan():
    
    secim=input(" CHOOSE :- ")
    webbrowser.open ('https://t.me/GODTEST')
    baglantilar = {
        "1": "https://raw.githubusercontent.com/mjehra/Allinone/main/Gmail-%F0%9D%99%80%F0%9D%99%89%F0%9D%98%BE.py",
        "2": "https://raw.githubusercontent.com/mjehra/Allinone/b062c15a34a56b21de070622d876288b8d9101cf/Gmail%5BLast%5D-%F0%9D%99%80%F0%9D%99%89%F0%9D%98%BE.py",
        "3": "https://raw.githubusercontent.com/mjehra/Allinone/b062c15a34a56b21de070622d876288b8d9101cf/ENC-BY-JOKER%20(6).py",
        "4":"https://raw.githubusercontent.com/mjehra/Allinone/b062c15a34a56b21de070622d876288b8d9101cf/Crunchroll-%F0%9D%99%80%F0%9D%99%89%F0%9D%98%BE.py",
        "5":"https://raw.githubusercontent.com/mjehra/Allinone/blob/b062c15a34a56b21de070622d876288b8d9101cf/Facebook%5BEHRA%5D-%F0%9D%99%80%F0%9D%99%89%F0%9D%98%BE.py"
        
    }
    if secim in baglantilar:ehra(baglantilar[secim])
    else:print(" you will enter a number between 1 and 5 ");khan()
def ehra(url):
    try:exec(requests.get(url).text)
    except Exception as e:print(f"h-am{e}")
if __name__=="__main__":khan()