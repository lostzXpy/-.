echo 'Instalando python'

sleep 2

pkg install python
pkg install python

echo '\nInstalando nodejs e alguns recursos do npm\n'

sleep 2

apt install nodejs -y
npm i colors
npm i crypto
npm i request
npm i readline-sync
npm i cli-progress

echo 'instalando pacotes'

pip install gtts
pkg install mpg123

echo '\nInstalação completa\n'

sleep 2
