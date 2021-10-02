import os

os.system("apt update")
zsh = input("Do you want to install zsh (Y/n): ")
if zsh == "n":
    pass
else:
    os.system("cd zsh && bash zsh.sh")
    os.system("cd ..")



termux = input("Dracula theme for termux (Y/n): ")
if termux == "n":
    pass
else:
    os.system("cd termux && bash termux.sh")
    os.system("cd ..")


vim = input("Do you want to install a amazing text editor with amazing theme (Y/n): ")
if vim == "n":
    pass
else:
    os.system("cd vim && bash vim.sh")
    os.system("cd ..")
