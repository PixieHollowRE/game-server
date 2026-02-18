@echo off
title Pixie Hollow - OTP Server
cd /d "%~dp0..\..\config"

:main
set DEBUG=*
"%~dp0..\..\otpd\otpgo" otp.yml
pause
goto :main
