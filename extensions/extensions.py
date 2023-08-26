file = input("File name: ").strip()
last = file.split(".")[-1]

if last == "gif":
    print("image/"+last)
elif last == "jpg" or last == "jpeg":
    print("image/jpeg")
elif last == "png":
    print("image/"+last)
elif last == "pdf" or last == "PDF":
    print("application/pdf")
elif last == "txt":
    print("text/plain")
elif last == "zip":
    print("application/"+last)
else:
    print("application/octet-stream")
