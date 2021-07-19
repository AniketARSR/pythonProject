import os

androidPath = input("Android File Path : ")
# iosPath = input("iOS Info File Path : ")

packageNamePath = input("Package Name Path :")
newPackageNamePath = input("New Package Name Path :")

os.rename(packageNamePath, newPackageNamePath)
packageName = input("Package Name To Change : ")
versionName = input("Version Name To Change : ")

texts_to_replace = {'com.natifi.storifi': packageName, '1.0.0': versionName}

with open(androidPath, 'r') as f:
    text = f.read()
    for replaceText in texts_to_replace:
        text = text.replace(replaceText, texts_to_replace[replaceText])
        with open(androidPath, 'w') as f:
            f.write(text)

# with open(iosPath, 'r') as f:
#     text = f.read()
#     for replaceText in texts_to_replace:
#         text = text.replace(replaceText, texts_to_replace[replaceText])
#         with open(iosPath, 'w') as f:
#            f.write(text)
