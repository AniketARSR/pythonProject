import requests
import base64
import os

userID = input("Please Enter UserID of App : ")
file_Path = input("Enter the Location to Save File : ")

response = requests.post("https://api.storifi.app/shopify-notifications/fetch-credentials",
                         data={"userId": "603b906e67e20993f0ad6106"})
data = response.json()
print(response.json())

# print("Encrypted Android File - " + data["data"]["configAndroid"])
print("Decrypted Android File - " + base64.b64decode(data["data"]["configAndroid"]).decode('utf-8'))
androidFileContent = base64.b64decode(data["data"]["configAndroid"]).decode('utf-8')
filepath = os.path.join(file_Path, 'google-serviceTest.json')
if not os.path.exists(file_Path):
    os.makedirs(file_Path)
f = open(filepath, "a")
f.write(androidFileContent)
f.close()

file = open(filepath, 'r')
print(file.read())
print("Google Service File Saved")
