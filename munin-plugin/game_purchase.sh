#!/bin/bash

SELF=`readlink -f $0`
DIR=`dirname "$SELF"`
PYTHON="$DIR/../env/bin/python"
SCRIPT="$DIR/game_purchase.py"

if [ "$1" == "autoconf" ]
then
    echo "yes"
    exit 0
fi

if [ "$1" = "config" ]
then
    "$PYTHON" "$SCRIPT" config
    exit 0
fi


"$PYTHON" "$SCRIPT"
