#!/bin/bash

function create_and_intialise() {
    python3 -m venv $1
    source $1/bin/activate
    pip install -r requirements.txt
    source .env
    python create.py $1
    echo "Folder is created"
    cd $FILEPATH$1
    git init
    echo "Git intialise complete"
    git remote add origin git@github.com:$USERNAME/$1.git
    echo "remote repo added"
    touch README.md
    git add .
    git commit -m "Initial commit"
    echo "Change commited locally"
    git push -u origin master
    echo "Change pushed successfully"
    code .
}