import os
from datetime import date

today = date.today().strftime("%d-%B-%Y")

def pusher():
    os.system("git add .")
    os.system('git commit -m "Committed on : {today} "'.format(today=today))
    os.system("git push origin main")

def append():
    file1 = open("myfile.txt", "a")
    file1.write(f"Modified on : {today} \n")
    file1.close()
    
    file1 = open("myfile.txt", "r")
    print("Output of Readlines after appending")
    print(file1.read())
    print()
    file1.close()

pusher()