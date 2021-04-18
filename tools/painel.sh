echo "\nInstalando recursos\n"

pkg update && pkg upgrade -y
pkg install git -y
pkg install python -y
pkg install python2 -y
pkg install python3 -y
git clone https://github.com/Kiny-Kiny/Kiny-Painel
cd Kiny-Painel
python3 main.py
