#!/bin/sh
cd ../../config

while true
do
  ../otpd/otpgo otp.yml
  sleep 5
done
