@echo off
set /p HAS_PYTHON=Do you already have Python installed? (y/n): 

if /I "%HAS_PYTHON%"=="n" (
    set PYTHON_URL=https://www.python.org/ftp/python/3.13.6/python-3.13.6-amd64.exe
    set PYTHON_INSTALLER=%TEMP%\python_installer.exe
    powershell -Command "Invoke-WebRequest -Uri %PYTHON_URL% -OutFile %PYTHON_INSTALLER%"
    %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1
    timeout /t 10
    python -m ensurepip --upgrade
)

python -m pip install --upgrade pip
python -m pip install requests colorama
python tool.py
pause
