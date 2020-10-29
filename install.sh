#!/bin/bash

declare -a pkgs=("tk" "PySimpleGUI" "pandas")

for i in ${pkgs[@]}; do
    pip3 show $i > /dev/null 2>&1
    printf "Checking $i ==> "
    if [ $? == 0 ]; then
        echo "Requirement already satisfied."
    else
        pip3 install $i
    fi
done

if echo "$SHELL" | grep -q "zsh"; then
    printf "\n%s\n" "alias merge_csv='python3 $PWD/merge_csv.py 1> /dev/null'" >> ~/.zshrc
    zsh
elif echo "$SHELL" | grep -q "bash"; then
    printf "\n%s\n" "alias merge_csv='python3 $PWD/merge_csv.py 1> /dev/null'" >> ~/.bashrc
    bash
fi

echo "Successfully installed!"
