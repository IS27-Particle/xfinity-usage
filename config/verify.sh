#!/bin/sh

read -p "Enter the verification code: " code
echo $code > /config/verification.txt