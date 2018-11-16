#!/bin/bash
FILENAME="plan-$(date +%Y-%m-%d).txt"
cd ~/Documents/Life/Plans/
touch $FILENAME
open $FILENAME
