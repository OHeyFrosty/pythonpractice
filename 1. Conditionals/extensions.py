file = input("File Name: ").strip().lower()
if ".gif" in file:
    print("image/gif")
elif ".jpg" in file or ".jpeg" in file:
    print("image/jpeg")
elif ".png" in file:
    print("image/png")
elif ".pdf" in file:
    print("application/pdf")
elif ".zip" in file:
    print("application/zip")
elif ".txt" in file:
    print("text/txt")
else:
    print("application/octet-stream")


    



"""
.gif image
.jpg image
.jpeg image
.png image
.pdf application
.zip application
.txt text


"""