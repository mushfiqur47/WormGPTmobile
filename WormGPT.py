import requests
import os
import sys
import pyfiglet
from tqdm import tqdm
from time import sleep

# = = = = = = = = = = = =

Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\033[2;36m'  # سمائي
Y = '\033[1;34m'  # ازرق فاتح

# = = = = = = = = = = = =



def vx(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.01)

while True:
    logo = pyfiglet.figlet_format('* WormGPT *')
    vx(A+logo+'                  Div By : @BLACK_DEMON_VX')
    
    print('')
    text1 = input(Y + "What's your Question: " + B)

    print('')
    for _ in tqdm(range(100), desc="Loading", unit="wait"):
        sleep(0.1)

    url = "https://dev-gpts.pantheonsite.io/wp-admin/js/apis/WormGPT.php?text={}".format(text1)
    response = requests.get(url)

    try:
        response.raise_for_status()
        answers = response.text
        #os.system('clear')
        vx(F + "The Answer: " + Z + answers)
        print('')
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)
