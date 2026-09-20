#!/bin/sh
screen -dmS OTP ./start_otp_server.sh
screen -dmS UberDOG ./start_uberdog.sh

cd ../..

screen -dmS Districts python3 -m DistrictStarter
