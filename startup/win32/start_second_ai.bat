@echo off
title Pixie Hollow - AI
cd ../..
set /P PYTHON_PATH=<PYTHON_PATH

set want_district_2=1

:main
%PYTHON_PATH% -m game.fairies.ai.AIStart config/config.prc
pause
goto :main
