#!/bin/sh
screen -dmS OTP ./start_otp_server.sh

cd ../..
screen -dmS UberDOG ./start_uberdog.sh
screen -dmS Districts python3 -m DistrictStarter
