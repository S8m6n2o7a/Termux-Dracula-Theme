import os



omz = input("Do You have oh-my-zsh and zsh in your system (Y/n): ").lower()


if omz == 'n':
    os.system('sudo apt install -y zsh')
    os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
elif omz == 'y' or omz == 'Y':
    pass
else:
    print("wrong Input")

os.system("git clone https://github.com/dracula/zsh.git")
os.system("ln -s $DRACULA_THEME/dracula.zsh-theme $OH_MY_ZSH/themes/dracula.zsh-theme")

