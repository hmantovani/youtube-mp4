@echo off
echo Gerenciando ambiente Python...
python -m venv venv
call venv\Scripts\activate
echo Instalando dependencias...
pip install -r requirements.txt --quiet

echo Abrindo o app e fechando este terminal...
:: O comando 'start' inicia o processo e permite que o .bat continue
:: O 'pythonw' roda o script sem abrir uma janela de comando preta
start pythonw main.py

:: Fecha o terminal imediatamente
exit