#!/bin/sh
screen -dmS OTP ./start_otp_server.sh

cd ../..
screen -dmS UberDOG python3 -m game.fairies.uberdog.Start config/config.prc
screen -dmS Districts python3 -m DistrictStarter
