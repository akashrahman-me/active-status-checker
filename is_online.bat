@echo off

:loop
REM Activate the virtual environment (using relative path)
call %~dp0\venv\Scripts\activate.bat

REM Run your Python script (using relative path)
python %~dp0\app.py

timeout /t 7200 /nobreak >nul
goto loop
