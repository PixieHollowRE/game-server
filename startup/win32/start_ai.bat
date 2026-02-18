@echo off
title Pixie Hollow - AI
cd /d "%~dp0..\.."
set /P PYTHON_PATH=<PYTHON_PATH

:main
%PYTHON_PATH% -m game.fairies.ai.AIStart config/config.prc
pause
goto :main
