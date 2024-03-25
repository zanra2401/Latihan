#!bin/bash

m=$1

$(git init)
$(git remote add origin https://github.com/zanra2401/alin)
$(git pull origin main)
$(git add .)
$(git commit -m "${m}")
