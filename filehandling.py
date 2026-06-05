try:
    file = int(input("Enter a file name!"))
    open("file", "r")
except:
    print("File not found!")
finally:
    print("Done!")
    



