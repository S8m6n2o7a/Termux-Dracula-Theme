import os

os.system("pkg update")
os.system("apt update --fix-missing")
os.system("pkg install -y toilet")
os.system("apt update --fix-missing")

termux = input("Dracula theme for termux (Y/n): ")
if termux == "n":
    pass
else:
    os.system("apt update --fix-missing")
    os.system("cd termux && bash termux.sh")
    os.system("apt update --fix-missing")
    os.system("cd ..")
    os.system("apt update --fix-missing")

    
vim = input("Do you want to install a amazing text editor with amazing theme (Y/n): ")
if vim == "n":
    pass
else:
    os.system("apt update --fix-missing")
    os.system("cd vim && bash vim.sh")
    os.system("apt update --fix-missing")
    os.system("cd ..")
    os.system("apt update --fix-missing")
    
zsh = input("Do you want to install zsh (Y/n): ")
if zsh == "n":
    pass
else:
    os.system("apt update --fix-missing")
    os.system("cd zsh && bash zsh.sh")
    os.system("apt update --fix-missing")
    os.system("cd")
    os.system("apt update --fix-missing")
