from shutil import copyfile, copytree
import os
import time


os.system("pkg install toilet")
BASEPATH = os.getcwd()

scriptCreator= '''
*******Termux Theme Changer*******
*   This Script Was Created by   *
*             Yougraj            *
**********************************
'''
source = '''
*****************Source*******************
*                Dracula Theme           *
*         https://draculatheme.com/      *
******************************************
*           Vim Plugin Manager           *
*  https://github.com/junegunn/vim-plug  *
******************************************
*        vimrc file created by           *
* https://gist.github.com/miguelgrinberg *
******************************************
'''
print(scriptCreator)
print(source)
os.system("toilet -f term -F border --gay 'Hola, soy Yougraj Mucho Gusto'")
time.sleep(3)

#***********************Update**************************
def update():
    up = ["pkg update", "apt update --fix-missing"]
    for i in up:
        os.system(i)


#**********************Termux***************************
def termux():
    update()
    os.chdir(BASEPATH)
    os.system("git clone https://github.com/dracula/termux.git")
    os.chdir("termux")
    original = "colors.properties"
    target = "/data/data/com.termux/files/home/.termux/colors.properties"
    copyfile(original, target)


#*************************Vim***************************
def vim():
    update()
    os.chdir(BASEPATH)
    os.system("curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
                   https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim")
    time.sleep(3)
    copyfile(".vimrc", "/data/data/com.termux/files/home/.vimrc")


#**************************Zsh**************************
def zsh():
    update()
    os.chdir(BASEPATH)
    os.system("pkg install -y zsh")


    #Installing Oh-My-Zsh
    os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
    time.sleep(3)
    os.remove("/data/data/com.termux/files/home/.zshrc")
    copyfile(".zshrc", "/data/data/com.termux/files/home/.zshrc")
   
   
   
    #Installing Dracula theme
    os.system("git clone https://github.com/dracula/zsh.git")
    os.chdir("zsh")
    copyfile("dracula.zsh-theme", "/data/data/com.termux/files/home/.oh-my-zsh/themes/dracula.zsh-theme")
    copytree("lib", "/data/data/com.termux/files/home/.oh-my-zsh/themes/lib")
    update()


#***********************SetUpScript*********************
def setUp():
    termux_install = input("Dracula theme for termux (Y/n): ")
    if termux_install == "n":
        pass
    else:
        termux()
    vim_install = input("Do you want to install a amazing text editor with amazing theme (Y/n): ")
    if vim_install == "n":
        pass
    else:
        vim()
    zsh_install = input("Do you want to install zsh (Y/n): ")
    if zsh_install == "n":
        pass
    else:
        zsh()

if __name__ == "__main__":
    setUp()
