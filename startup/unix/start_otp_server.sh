#!/bin/sh
cd ../../config

while true
do
  ../OtpGo/otpgo otp.yml
  sleep 5
done
