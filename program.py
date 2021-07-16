import os

def pusher():
    

def append():
    file1 = open("myfile.txt", "a")  # append mode
    file1.write("Today \n")
    file1.close()
    
    file1 = open("myfile.txt", "r")
    print("Output of Readlines after appending")
    print(file1.read())
    print()
    file1.close()
    

    file1.close()