#!/bin/bash

SELF=`readlink -f $0`
DIR=`dirname "$SELF"`
PYTHON="$DIR/../env/bin/python"

if [ "$1" == "autoconf" ]
then
    echo "yes"
    exit 0
fi


if [ "$1" = "config" ]
then
    "$PYTHON" "$DIR/game_servers.py" config
    exit 0
fi


"$PYTHON" "$DIR/game_servers.py"

