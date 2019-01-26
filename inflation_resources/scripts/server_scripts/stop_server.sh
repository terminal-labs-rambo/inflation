#!/usr/bin/env bash

uname | grep 'Darwin' &> /dev/null
if [ $? == 0 ]; then
  if [[ $(netstat -anp tcp | awk '$6 == "LISTEN" && $4 ~ /\.5000$/') ]]; then
    kill `lsof -t -i:5000`
  fi
else
  if [[ $(netstat -lnt | awk '$6 == "LISTEN" && $4 ~ /\.5000$/') ]]; then
    kill `lsof -t -i:5000`
  fi
fi
